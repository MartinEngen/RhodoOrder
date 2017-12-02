# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-02 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderSchema', '0003_order_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='link',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=100, verbose_name='Pris (Per Plante)'),
        ),
    ]
