
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from rest_framework.permissions import IsAuthenticated, IsAdminUser  # , AllowAny

from manufacturers.models import Manufacturer, Product
from manufacturers.serializers import ManufacturerSerializer, ProductSerializer

from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ManufacturerListApiView(ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    filterset_fields = ("country",)
    permission_classes = (IsAuthenticated, IsAdminUser,)


class ManufacturerDetailApiView(RetrieveAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class ManufacturerCreateApiView(CreateAPIView):
    serializer_class = ManufacturerSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class ManufacturerUpdateApiView(UpdateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = (IsAdminUser,)


class ManufacturerDeleteApiView(DestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = (IsAdminUser,)


class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class ProductDetailApiView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class ProductCreateApiView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class ProductUpdateApiView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser,)


class ProductDeleteApiView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser,)
