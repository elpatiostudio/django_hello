# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    # fields = ('name', 'instrument',)
    list_display = ('name', 'type_of_product', 'price' )
    search_fields = ('name', 'description', 'type_of_product__name',)
    list_filter = ('type_of_product',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
