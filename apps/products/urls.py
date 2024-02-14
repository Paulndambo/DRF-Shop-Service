from django.urls import path

from apps.products.views import (MultipleProductLoadingAPIView,
                                 ProductListCreateAPIView,
                                 ProductLogListAPIView,
                                 ProductRetrieveUpdateDestroyAPIView,
                                 ProductsUploadAPIView)

urlpatterns = [
    path("", ProductListCreateAPIView.as_view(), name="products"),
    path("<int:pk>/", ProductRetrieveUpdateDestroyAPIView.as_view(), name="product-details"),
    path("load-multiple-products/", MultipleProductLoadingAPIView.as_view(), name="load-multiple-products"),
    path("products-upload/", ProductsUploadAPIView.as_view(), name="products-upload"),
    path("product-logs/", ProductLogListAPIView.as_view(), name="product-logs"),
]