
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from rest_framework.permissions import IsAuthenticated, IsAdminUser  # , AllowAny

from sellers.models import Seller
from sellers.serializers import SellerSerializer


class SellerListApiView(ListAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    filterset_fields = ("country",)
    permission_classes = (IsAuthenticated, IsAdminUser,)


class SellerDetailApiView(RetrieveAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class SellerCreateApiView(CreateAPIView):
    serializer_class = SellerSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class SellerUpdateApiView(UpdateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class SellerDeleteApiView(DestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = (IsAdminUser,)
