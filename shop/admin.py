from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count_now']


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['product', 'person', 'address', 'date']


admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
