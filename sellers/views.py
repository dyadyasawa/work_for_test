
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from rest_framework.permissions import IsAuthenticated  # , AllowAny, IsCreator

from sellers.models import Seller
from sellers.serializers import SellerSerializer


class SellerListApiView(ListAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    filterset_fields = ("country",)


class SellerDetailApiView(RetrieveAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #     pk = kwargs("pk",)
    #     return Manufacturer.objects.get(pk=pk)


class SellerCreateApiView(CreateAPIView):
    serializer_class = SellerSerializer
    # permission_classes = (IsAuthenticated,)

    # def perform_create(self, serializer):
    #     """Делаем текущего пользователя 'Создателем' Производителя."""
    #     new_manufacturer = serializer.save()
    #     new_manufacturer.creator = self.request.user
    #     new_manufacturer.save()


class SellerUpdateApiView(UpdateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    # permission_classes = (
    #     IsAuthenticated,
    #     IsCreator,
    # )

    # def get_queryset(self, pk):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Manufacturer.objects.filter(pk=pk)


class SellerDeleteApiView(DestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    # permission_classes = (IsCreator,)

    # def get_queryset(self, pk):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Manufacturer.objects.filter(pk=pk)

