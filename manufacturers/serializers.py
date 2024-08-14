
from rest_framework import serializers

from manufacturers.models import Manufacturer


class ManufacturerSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Manufacturer."""

    class Meta:
        model = Manufacturer
        fields = "__all__"

        # validators = [
        #     NotCombinationValidator("connection_habit", "reward"),
        #     TimeDurationValidator("duration"),
        #     CombinationValidator("connection_habit", "habit_is_pleasant"),
        #     AbsenceValidator("habit_is_pleasant", "connection_habit", "reward"),
        #     FrequencyValidator("number_of_executions"),
        # ]
