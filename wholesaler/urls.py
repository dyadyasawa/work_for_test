
from django.urls import path

# from rest_framework.permissions import AllowAny
from wholesaler.apps import WholesalerConfig

from wholesaler.views import (
    WholesalerListApiView,
    WholesalerDetailApiView,
    WholesalerCreateApiView,
    WholesalerUpdateApiView,
    WholesalerDeleteApiView,
)

app_name = WholesalerConfig.name

urlpatterns = [

    path("list/", WholesalerListApiView.as_view(), name="manufacturers-list"),
    path("detail/<int:pk>/", WholesalerDetailApiView.as_view(), name="manufacturers-detail"),
    path("create/", WholesalerCreateApiView.as_view(), name="manufacturers-create"),
    path("update/<int:pk>/", WholesalerUpdateApiView.as_view(), name="manufacturers-update"),
    path("delete/<int:pk>/", WholesalerDeleteApiView.as_view(), name="manufacturers-delete"),

]



