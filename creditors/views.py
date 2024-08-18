
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from rest_framework.permissions import IsAuthenticated  # , AllowAny, IsCreator

from creditors.models import Creditor
from creditors.serializers import CreditorSerializer


class CreditorListApiView(ListAPIView):
    queryset = Creditor.objects.all()
    serializer_class = CreditorSerializer
    # pagination_class = CustomPagination
    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return Manufacturer.objects.all()


class CreditorDetailApiView(RetrieveAPIView):
    queryset = Creditor.objects.all()
    serializer_class = CreditorSerializer
    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #     pk = kwargs("pk",)
    #     return Manufacturer.objects.get(pk=pk)


class CreditorCreateApiView(CreateAPIView):
    serializer_class = CreditorSerializer
    # permission_classes = (IsAuthenticated,)

    # def perform_create(self, serializer):
    #     """Делаем текущего пользователя 'Создателем' Производителя."""
    #     new_manufacturer = serializer.save()
    #     new_manufacturer.creator = self.request.user
    #     new_manufacturer.save()


class CreditorUpdateApiView(UpdateAPIView):
    queryset = Creditor.objects.all()
    serializer_class = CreditorSerializer
    # permission_classes = (
    #     IsAuthenticated,
    #     IsCreator,
    # )

    # def get_queryset(self, pk):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Manufacturer.objects.filter(pk=pk)


class CreditorDeleteApiView(DestroyAPIView):
    queryset = Creditor.objects.all()
    serializer_class = CreditorSerializer
    # permission_classes = (IsCreator,)

    # def get_queryset(self, pk):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Manufacturer.objects.filter(pk=pk)

