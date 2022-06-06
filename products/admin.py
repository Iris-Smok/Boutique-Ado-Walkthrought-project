""" admin.py """
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """ product model display """
    list_display = (
        'sku',
        'name',
        'category',
        'rating',
        'image'
    )

    ordering = ('sku')


class CategoryAdmin(admin.ModelAdmin):
    """ category model displat """
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
