# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Show


class ShowAdmin(admin.ModelAdmin):
    # fields = ('name', 'instrument',)
    list_display = ('location', 'name', 'date', 'description')
    search_fields = ('name', 'location', 'date',)
    list_filter = ('location',)

admin.site.register(Show, ShowAdmin)
