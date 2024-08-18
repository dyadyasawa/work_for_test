
from rest_framework import serializers

from creditors.models import Creditor


class CreditorSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Creditor."""

    class Meta:
        model = Creditor
        fields = "__all__"
