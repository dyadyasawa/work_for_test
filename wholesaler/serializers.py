
from rest_framework import serializers

from wholesaler.models import Wholesaler


class WholesalerSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Wholesaler."""

    class Meta:
        model = Wholesaler
        fields = "__all__"
