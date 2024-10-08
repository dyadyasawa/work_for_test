
from rest_framework import serializers  # ModelSerializer, SerializerMethodField

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

