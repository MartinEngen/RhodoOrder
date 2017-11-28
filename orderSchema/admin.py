# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import models
from django.contrib import admin


class ProductsInline(admin.TabularInline):
    model = models.Product
    fk_name = 'order'

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductsInline,
    ]

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Product)
admin.site.register(models.Order, OrderAdmin)
