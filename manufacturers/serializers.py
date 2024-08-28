
from rest_framework import serializers

from manufacturers.models import Manufacturer, Product


class ManufacturerSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Manufacturer."""

    class Meta:
        model = Manufacturer
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Product."""

    class Meta:
        model = Product
        fields = "__all__"
