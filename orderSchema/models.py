# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    email = models.EmailField('Epost Adresse', primary_key=True, max_length=100)
    first_name = models.CharField('Fornavn', max_length=100)
    last_name = models.CharField('Etternavn', max_length=100)
    phone_number = models.CharField('Telefonnummer', max_length=12)

class Order(models.Model):
    def __str__(self):
        return self.customer.first_name + ' ' + self.customer.last_name.encode('utf-8') + ' ' + str(self.order_date).encode('utf-8')

    def __unicode__(self):
        return self.customer.first_name + ' ' + self.customer.last_name.encode('utf-8') + ' ' + str(self.order_date)

    order_date = models.DateField('Bestilligns dato', auto_now_add=True)
    customer = models.ForeignKey(Customer, verbose_name='Kunde', related_name='Kunde', on_delete=models.CASCADE)

class Product(models.Model):
    def __str__(self):
        return unicode(self.plant_name) + ' ' + unicode(self.size)

    def __unicode__(self):
        return unicode(self.plant_name) + ' ' + unicode(self.size)

    order = models.ForeignKey(Order)
    plant_name = models.CharField('Plane Navn', max_length=255)
    size = models.CharField('Størrelse', max_length=100)
    amount = models.IntegerField('Antall', default=0)
    price = models.IntegerField('Pris (Per Plante)', default=0)
    link = models.CharField('Lenke til plante', max_length=255)

