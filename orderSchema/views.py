# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from django.shortcuts import render
from .forms import plantForm, OrderForm
from django.forms import formset_factory
from .models import Customer, Order, Product


# Create your views here.
def order(request):
    if (request.method == 'POST'):
        print(request.POST)
        myForm = OrderForm(request.POST)

        print(myForm.is_valid())
        if (myForm.is_valid()):
            print("Valid Form!.")

            print(request.POST)
            first_name = myForm.cleaned_data['first_name']
            last_name = myForm.cleaned_data['last_name']
            email = myForm.cleaned_data['email']
            phone_number = myForm.cleaned_data['phone_number']
            misc_info = myForm.cleaned_data['misc_info']

            currentCustomer, created = Customer.objects.update_or_create(pk=email,
                                                                         defaults={'first_name': first_name,
                                                                                   'last_name': last_name,
                                                                                   'phone_number': phone_number})

            currentOrder = Order(customer=currentCustomer)
            currentOrder.save()

            plantNameList = request.POST.getlist('plantName')
            plantPriceList = request.POST.getlist('price')
            plantAmountList = request.POST.getlist('amount')
            plantSizeList = request.POST.getlist('size')
            plantsInOrder = len(plantNameList)

            for x in range(0, plantsInOrder):
                currentPlantName = ''
                currentPlantSize = ''
                currentPlantAmount = 0
                currentPlantPrice = 0

                # Not trusting these users, need this to run no matter what..
                try:
                    currentPlantName = plantNameList[x]
                except IndexError:
                    logging.warning("Name - Out of Index Error")

                try:
                    currentPlantSize = plantSizeList[x]
                except IndexError:
                    logging.warning("Size - Out of Index Error")

                try:
                    currentPlantAmount = plantAmountList[x]
                except IndexError:
                    logging.warning("Amount - Out of Index Error")

                try:
                    currentPlantPrice = plantPriceList[x]
                except IndexError:
                    logging.warning("Price - Out of Index Error")


                currentProduct = Product(order=currentOrder, plant_name=currentPlantName, size=currentPlantSize, amount=currentPlantAmount, price=currentPlantPrice)
                currentProduct.save()



        ##plantFormSet = formset_factory(plantForm)

        # myPlants = plantFormSet(request.POST)
        # print(myPlants)
    return render(request, 'orderSchema/order.html')
