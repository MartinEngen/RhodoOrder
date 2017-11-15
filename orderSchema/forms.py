    # -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator
import datetime
from django.forms import formset_factory



# Plants
class plantForm(forms.Form):
    plant_name = forms.CharField(max_length=255)
    size = forms.CharField(max_length=255)  # forms.CharField('Størrelse', max_length=100)
    amount = forms.CharField(max_length=255)  # forms.IntegerField('Antall', default=0)
    price = forms.CharField(max_length=255)  # forms.IntegerField('Pris (Per Plante)', default=0)
    link = forms.CharField(max_length=255)  # forms.CharField('Lenke til plante', max_length=255)



class OrderForm(forms.Form):
    first_name = forms.CharField(label='Fornavn', max_length=100, required=True)
    last_name = forms.CharField(label='Etternavn', max_length=100, required=True)

    email = forms.EmailField(label='Epost adresse', max_length=100, required=True)
    phone_number = forms.CharField(max_length=12, validators=[RegexValidator(r'^\d{1,10}$')], required=True)

    misc_info = forms.CharField(label='Ekstra informasjon (Maks 255 Karakterer)', max_length=255, required=False)


    #Essential information for the Booking.
    plantName = forms.CharField(max_length=255, required=False)
    size = forms.CharField(max_length=255, required=False)
    amount = forms.CharField(max_length=255, required=False)
    price = forms.CharField(max_length=255, required=False)
