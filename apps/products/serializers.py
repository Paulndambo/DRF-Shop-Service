from rest_framework import serializers

from apps.products.models import Product, ProductLog


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLog
        fields = "__all__"



class ProductsUploadSerializer(serializers.Serializer):
    products_file = serializers.FileField()


class MultipleProductLoadingSerializer(serializers.Serializer):
    products_data = serializers.JSONField(default=list)