
from rest_framework import serializers

from wholesaler.models import Wholesaler


class WholesalerSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Wholesaler."""

    class Meta:
        model = Wholesaler
        fields = "__all__"

        # validators = [
        #     NotCombinationValidator("connection_habit", "reward"),
        #     TimeDurationValidator("duration"),
        #     CombinationValidator("connection_habit", "habit_is_pleasant"),
        #     AbsenceValidator("habit_is_pleasant", "connection_habit", "reward"),
        #     FrequencyValidator("number_of_executions"),
        # ]

