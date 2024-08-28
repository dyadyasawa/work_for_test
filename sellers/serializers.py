
from rest_framework import serializers

from sellers.models import Seller


class SellerSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Seller."""

    class Meta:
        model = Seller
        fields = "__all__"
