
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from rest_framework.permissions import IsAuthenticated  # , AllowAny, IsCreator

from manufacturers.models import Manufacturer
from manufacturers.serializers import ManufacturerSerializer


class ManufacturerListApiView(ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    # pagination_class = CustomPagination
    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return Manufacturer.objects.all()


class ManufacturerDetailApiView(RetrieveAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #     pk = kwargs("pk",)
    #     return Manufacturer.objects.get(pk=pk)


class ManufacturerCreateApiView(CreateAPIView):
    serializer_class = ManufacturerSerializer
    # permission_classes = (IsAuthenticated,)

    # def perform_create(self, serializer):
    #     """Делаем текущего пользователя 'Создателем' Производителя."""
    #     new_manufacturer = serializer.save()
    #     new_manufacturer.creator = self.request.user
    #     new_manufacturer.save()


class ManufacturerUpdateApiView(UpdateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    # permission_classes = (
    #     IsAuthenticated,
    #     IsCreator,
    # )

    # def get_queryset(self, pk):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Manufacturer.objects.filter(pk=pk)


class ManufacturerDeleteApiView(DestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    # permission_classes = (IsCreator,)

    # def get_queryset(self, pk):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Manufacturer.objects.filter(pk=pk)
