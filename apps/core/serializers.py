from rest_framework import serializers

from apps.products.models import Product, ProductLog


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductLogSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    class Meta:
        model = ProductLog
        fields = "__all__"


    def get_product_name(self, obj):
        return obj.name