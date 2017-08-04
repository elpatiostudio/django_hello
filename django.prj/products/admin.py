# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Product

class ProductAdmin(admin.ModelAdmin):
    # fields = ('name', 'instrument',)
    list_display = ('name', 'type_of_product', 'price' )
    search_fields = ('name', 'description', 'type_of_products',)
    list_filter = ('type_of_product',)

admin.site.register(Product, ProductAdmin)