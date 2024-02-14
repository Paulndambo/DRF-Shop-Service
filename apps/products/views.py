import os

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from apps.core.shared_methods.file_reader import FileReaderMixin
from apps.products.models import Product, ProductLog
from apps.products.serializers import (MultipleProductLoadingSerializer,
                                       ProductLogSerializer, ProductSerializer,
                                       ProductsUploadSerializer)
from apps.products.upload_products import ProductUploadMixin

fs = FileSystemStorage(location='temp')


# Create your views here.
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field = "pk"


class ProductsUploadAPIView(generics.CreateAPIView):
    """
    This class allows the ability to upload products using either json or csv files

    """
    serializer_class = ProductsUploadSerializer


    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            data_file = request.FILES.get("products_file")

            file_content = data_file.read()
            source_file_content = ContentFile(file_content)
            source_file_name = fs.save(
                "temp_source_file.csv", source_file_content
            )
            temp_source_file = fs.path(source_file_name)

            file_reader = FileReaderMixin(temp_source_file)

            """
            Checking the file extension to determine which file reader method to invoke
            """
            data_file_extension = data_file.name.split('.')[-1].lower()

            file_data = []
           
            if data_file_extension == "csv":
                file_data = file_reader.read_csv_file()

            elif data_file_extension == "json":
                file_data = file_reader.read_json_file()
            
            if file_data:
                products_uploader = ProductUploadMixin(data=file_data)
                products_uploader.run()

            return Response({"message": "Products Successfully Uploaded"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MultipleProductLoadingAPIView(generics.CreateAPIView):
    serializer_class = MultipleProductLoadingSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            products_uploader = ProductUploadMixin(data=data["products_data"])
            products_uploader.run()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductLogListAPIView(generics.ListAPIView):
    queryset = ProductLog.objects.all()
    serializer_class = ProductLogSerializer
    