# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderSchema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderSchema.Order'),
        ),
    ]