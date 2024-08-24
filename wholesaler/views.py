

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from rest_framework.permissions import IsAuthenticated, IsAdminUser  # , AllowAny, IsCreator

from wholesaler.models import Wholesaler
from wholesaler.serializers import WholesalerSerializer


class WholesalerListApiView(ListAPIView):
    queryset = Wholesaler.objects.all()
    serializer_class = WholesalerSerializer
    filterset_fields = ("country",)
    # pagination_class = CustomPagination
    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return Manufacturer.objects.all()


class WholesalerDetailApiView(RetrieveAPIView):
    queryset = Wholesaler.objects.all()
    serializer_class = WholesalerSerializer
    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #     pk = kwargs("pk",)
    #     return Manufacturer.objects.get(pk=pk)


class WholesalerCreateApiView(CreateAPIView):
    serializer_class = WholesalerSerializer
    # permission_classes = (IsAuthenticated,)

    # def perform_create(self, serializer):
    #     """Делаем текущего пользователя 'Создателем' Производителя."""
    #     new_manufacturer = serializer.save()
    #     new_manufacturer.creator = self.request.user
    #     new_manufacturer.save()


class WholesalerUpdateApiView(UpdateAPIView):
    queryset = Wholesaler.objects.all()
    serializer_class = WholesalerSerializer
    # permission_classes = (
    #     IsAuthenticated,
    #     IsCreator,
    # )

    # def get_queryset(self, pk):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Manufacturer.objects.filter(pk=pk)


class WholesalerDeleteApiView(DestroyAPIView):
    queryset = Wholesaler.objects.all()
    serializer_class = WholesalerSerializer
    # permission_classes = (IsCreator,)

    # def get_queryset(self, pk):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Manufacturer.objects.filter(pk=pk)
