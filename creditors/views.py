
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from rest_framework.permissions import IsAdminUser, IsAuthenticated  # , AllowAny

from creditors.models import Creditor
from creditors.serializers import CreditorSerializer


class CreditorListApiView(ListAPIView):
    queryset = Creditor.objects.all()
    serializer_class = CreditorSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class CreditorDetailApiView(RetrieveAPIView):
    queryset = Creditor.objects.all()
    serializer_class = CreditorSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class CreditorCreateApiView(CreateAPIView):
    serializer_class = CreditorSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class CreditorUpdateApiView(UpdateAPIView):
    queryset = Creditor.objects.all()
    serializer_class = CreditorSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class CreditorDeleteApiView(DestroyAPIView):
    queryset = Creditor.objects.all()
    serializer_class = CreditorSerializer
    permission_classes = (IsAuthenticated,)
