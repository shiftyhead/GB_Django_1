from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'category']
    list_filter = ['category']
    search_fields = ['name', 'snippet']


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory, ProductCategoryAdmin)
