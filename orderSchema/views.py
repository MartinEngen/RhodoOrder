# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from django.shortcuts import render
from .forms import plantForm, OrderForm
from django.forms import formset_factory
from .models import Customer, Order, Product
import math


def mk_int(s):
    s = s.strip()
    return int(s) if s else 1


# Create your views here.
def order(request):
    context = {}
    if (request.method == 'POST'):
        print(request.POST)
        myForm = OrderForm(request.POST)
        listOfPlants = []

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
            if not misc_info or misc_info == "":
                misc_info = "Ingen ekstra informasjon..."
            currentOrder = Order(customer=currentCustomer, misc_info=misc_info)
            currentOrder.save()

            plantNameList = request.POST.getlist('plantName')
            plantPriceList = request.POST.getlist('price')
            plantAmountList = request.POST.getlist('amount')
            plantSizeList = request.POST.getlist('size')
            plantsInOrder = len(plantNameList)
            count = 0
            for x in range(0, plantsInOrder):
                currentPlantName = ''
                currentPlantSize = ''
                currentPlantAmount = 0
                currentPlantPrice = 0

                # Not trusting these users, need this to run no matter what..
                try:
                    currentPlantName = plantNameList[x]

                    if currentPlantName == "" or not currentPlantName:
                        currentPlantName = 'Ikke oppgitt'
                except IndexError:
                    currentPlantName = 'Ikke oppgitt'
                    logging.warning("Name - Out of Index Error")

                try:
                    currentPlantSize = plantSizeList[x]

                    if currentPlantSize == "" or not currentPlantSize:
                        currentPlantSize = 'Ikke oppgitt'
                except IndexError:
                    currentPlantSize = 'Ikke oppgitt'
                    logging.warning("Size - Out of Index Error")

                try:
                    currentPlantAmount = mk_int(plantAmountList[x])
                except IndexError:
                    currentPlantAmount = 1
                    logging.warning("Amount - Out of Index Error")

                try:
                    currentPlantPrice = plantPriceList[x]

                    if currentPlantPrice == "" or not currentPlantPrice:
                        currentPlantPrice = 'Ikke Oppgitt'
                except IndexError:
                    currentPlantPrice = 'Ikke Oppgitt'
                    logging.warning("Price - Out of Index Error")


                currentProduct = Product(order=currentOrder, plant_name=currentPlantName, size=currentPlantSize, amount=currentPlantAmount, price=currentPlantPrice)
                if (not currentProduct.plant_name) and (not currentProduct.size) and (not currentProduct.price):
                    logging.warning("Empty Field - lets not save..")
                else:
                    count = count + 1
                    listOfPlants.append(currentProduct)
                    currentProduct.save()


            context = {
                'name': first_name,
                'orderId': currentOrder.id,
                'listOfPlants': listOfPlants,
                'count': count

            }
            #from mail_templated import send_mail

            #send_mail('orderSchema/email.tpl', {'name': first_name, 'listOfPlants': listOfPlants}, 'ikke.svar@hagevekster.no', [email, 'jo.engen@gmail.com', 'nitrax92@gmail.com'])
            return render(request, 'orderSchema/success.html', context)

        else:
            print(myForm.errors)
            context['error'] = True
            context['errorMessage'] = "Det var noe galt med angitt informasjon, fyll ut alle felter og prøv igjen"

    return render(request, 'orderSchema/order.html', context)
