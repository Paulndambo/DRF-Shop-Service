from django.db import models

from apps.core.models import AbstractBaseModel

PRODUCT_ACTION_CHOICES = (
    ("New Product Added", "New Product Added"),
    ("Damaged Product Removed", "Damaged Product Removed"),
    ("Product Sold", "Product Sold"),
    ("Product Deleted", "Product Deleted"),
    ("Product Re-Stocked", "Product Re-Stocked"),
)

# Create your models here.
class Product(AbstractBaseModel):
    name = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=100, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class ProductLog(AbstractBaseModel):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    action = models.CharField(max_length=255, choices=PRODUCT_ACTION_CHOICES)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} has been {self.action}"