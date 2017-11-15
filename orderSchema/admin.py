# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import models
from django.contrib import admin

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Product)
admin.site.register(models.Order)
