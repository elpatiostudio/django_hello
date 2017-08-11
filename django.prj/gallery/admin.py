# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Gallery


class GalleryAdmin(admin.ModelAdmin):
# fields = ('name', 'instrument',)
    list_display = ('caption', 'url',)
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Gallery, GalleryAdmin)
