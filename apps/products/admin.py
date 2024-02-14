from django.contrib import admin

from apps.products.models import Product, ProductLog


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "unit_price", "quantity"]


@admin.register(ProductLog)
class ProductLogAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "quantity", "action"]