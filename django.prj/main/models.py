# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Member(models.Model):
    name = models.TextField()