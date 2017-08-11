# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Category, Show


class ShowAdmin(admin.ModelAdmin):
    # fields = ('name', 'instrument',)
    list_display = ('location', 'name', 'date', 'description')
    search_fields = ('name', 'location', 'date',)
    list_filter = ('location',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Show, ShowAdmin)
admin.site.register(Category, CategoryAdmin)
