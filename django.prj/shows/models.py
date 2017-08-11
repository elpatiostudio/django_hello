# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Show(models.Model):
    location = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    departament_shows = models.ForeignKey(Category)
    date = models.CharField(max_length=200)
    description = models.TextField(default='', null=True, blank=True,)

    def __unicode__(self):
        return self.name