
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
    filterset_fields = ("country",)


class ManufacturerDetailApiView(RetrieveAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


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
