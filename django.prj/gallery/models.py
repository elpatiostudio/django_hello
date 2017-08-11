# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=80)
    caption = models.CharField(max_length=200)
    url =models.TextField(default='http://via.placeholder.com/200x200',)
    
    def __unicode__(self):
        return self.name




