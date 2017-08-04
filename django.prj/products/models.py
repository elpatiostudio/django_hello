# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    TYPE_CHOICES = (
    	('A', 'Apparel'),
    	('D', 'DVDs'),
    	('C', 'CDs'),
    	('O', 'Others'),
    	)
    type_of_product = models.CharField(max_length=1, choices=TYPE_CHOICES,) 
    description = models.TextField(default='', null=True, blank=True,)
    price = models.CharField(max_length=200, default='Not avaliable at the moment')

    def __unicode__(self):
    	return self.name

