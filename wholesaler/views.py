

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from wholesaler.models import Wholesaler
from wholesaler.serializers import WholesalerSerializer


class WholesalerListApiView(ListAPIView):
    queryset = Wholesaler.objects.all()
    serializer_class = WholesalerSerializer
    filterset_fields = ("country",)
    permission_classes = (IsAuthenticated, IsAdminUser)


class WholesalerDetailApiView(RetrieveAPIView):
    queryset = Wholesaler.objects.all()
    serializer_class = WholesalerSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)


class WholesalerCreateApiView(CreateAPIView):
    serializer_class = WholesalerSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)


class WholesalerUpdateApiView(UpdateAPIView):
    queryset = Wholesaler.objects.all()
    serializer_class = WholesalerSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class WholesalerDeleteApiView(DestroyAPIView):
    queryset = Wholesaler.objects.all()
    serializer_class = WholesalerSerializer
    permission_classes = (IsAdminUser,)
