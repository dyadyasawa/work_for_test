
from django.urls import path

# from rest_framework.permissions import AllowAny
from manufacturers.apps import ManufacturersConfig

from manufacturers.views import (
    ManufacturerListApiView,
    ManufacturerDetailApiView,
    ManufacturerCreateApiView,
    ManufacturerUpdateApiView,
    ManufacturerDeleteApiView,

    ProductListApiView,
    ProductDetailApiView,
    ProductCreateApiView,
    ProductUpdateApiView,
    ProductDeleteApiView,

)


app_name = ManufacturersConfig.name

urlpatterns = [

    path("list/", ManufacturerListApiView.as_view(), name="manufacturers-list"),
    path("detail/<int:pk>/", ManufacturerDetailApiView.as_view(), name="manufacturers-detail"),
    path("create/", ManufacturerCreateApiView.as_view(), name="manufacturers-create"),
    path("update/<int:pk>/", ManufacturerUpdateApiView.as_view(), name="manufacturers-update"),
    path("delete/<int:pk>/", ManufacturerDeleteApiView.as_view(), name="manufacturers-delete"),

    path("product_list/", ProductListApiView.as_view(), name="product-list"),
    path("product_detail/<int:pk>/", ProductDetailApiView.as_view(), name="product-detail"),
    path("product_create/", ProductCreateApiView.as_view(), name="product-create"),
    path("product_update/<int:pk>/", ProductUpdateApiView.as_view(), name="product-update"),
    path("product_delete/<int:pk>/", ProductDeleteApiView.as_view(), name="product-delete"),

]


