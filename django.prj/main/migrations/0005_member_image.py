# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-18 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170804_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='members/'),
        ),
    ]
