from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model')
    search_fields = ('brand', 'model')
    list_display_links = ('id', 'brand', 'model')


admin.site.register(Product, ProductAdmin)
