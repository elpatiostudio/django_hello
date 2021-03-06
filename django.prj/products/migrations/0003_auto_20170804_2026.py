# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-04 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170804_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type_of_product',
            field=models.CharField(choices=[('A', 'Apparel'), ('D', 'DVDs'), ('C', 'CDs'), ('O', 'Others')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(default='Not avaliable at the moment', max_length=200),
        ),
    ]
