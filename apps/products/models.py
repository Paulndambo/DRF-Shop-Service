from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    product = models.CharField(max_length=255, null=True)
    action = models.CharField(max_length=255, choices=PRODUCT_ACTION_CHOICES)
    quantity = models.IntegerField(default=0)

    #def __str__(self):
    #    return f"{self.product.name} has been {self.action}"



@receiver(post_save, sender=Product)
def create_product_log(sender, instance, created, **kwargs):
    if created:
        ProductLog.objects.create(
            product=instance.name,
            action="New Product Added",
            quantity=instance.quantity
        )