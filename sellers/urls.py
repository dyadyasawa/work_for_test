
from django.urls import path

# from rest_framework.permissions import AllowAny
from sellers.apps import SellersConfig
from sellers.views import (
    SellerListApiView,
    SellerDetailApiView,
    SellerCreateApiView,
    SellerUpdateApiView,
    SellerDeleteApiView,
)

app_name = SellersConfig.name

urlpatterns = [

    path("list/", SellerListApiView.as_view(), name="sellers-list"),
    path("detail/<int:pk>/", SellerDetailApiView.as_view(), name="sellers-detail"),
    path("create/", SellerCreateApiView.as_view(), name="sellers-create"),
    path("update/<int:pk>/", SellerUpdateApiView.as_view(), name="sellers-update"),
    path("delete/<int:pk>/", SellerDeleteApiView.as_view(), name="sellers-delete"),

]
