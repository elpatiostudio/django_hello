# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=200)
    instrument = models.CharField(max_length=200, default='')
    image = models.FileField(upload_to='members/', blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=GENDER_CHOICES[0][0])
    description = models.TextField(default='', null=True, blank=True,)

    def __unicode__(self):
        return self.name
