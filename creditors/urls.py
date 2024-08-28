
from django.urls import path

# from rest_framework.permissions import AllowAny
from creditors.apps import CreditorsConfig

from creditors.views import (
    CreditorListApiView,
    CreditorDetailApiView,
    CreditorCreateApiView,
    CreditorUpdateApiView,
    CreditorDeleteApiView,
)

app_name = CreditorsConfig.name

urlpatterns = [

    path("list/", CreditorListApiView.as_view(), name="creditors-list"),
    path("detail/<int:pk>/", CreditorDetailApiView.as_view(), name="creditors-detail"),
    path("create/", CreditorCreateApiView.as_view(), name="creditors-create"),
    path("update/<int:pk>/", CreditorUpdateApiView.as_view(), name="creditors-update"),
    path("delete/<int:pk>/", CreditorDeleteApiView.as_view(), name="creditors-delete"),

]



