# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    type_of_product = models.ForeignKey(Category)
    description = models.TextField(default='', null=True, blank=True,)
    price = models.CharField(max_length=200, default='Not avaliable at the moment')

    def __unicode__(self):
        return self.name
