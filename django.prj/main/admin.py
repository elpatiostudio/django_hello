# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Member


class MemberAdmin(admin.ModelAdmin):
    # fields = ('name', 'instrument',)
    list_display = ('name', 'gender', 'instrument',)
    search_fields = ('name', 'description', 'instrument',)
    list_filter = ('gender',)

admin.site.register(Member, MemberAdmin)
