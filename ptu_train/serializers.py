from rest_framework import serializers
from .models import TrainTerminal, TrainTimeTable


class TrainTerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainTerminal
        exclude = ("id",)


class TrainTimeTableSerializer(serializers.ModelSerializer):
    train_terminal = TrainTerminalSerializer()

    class Meta:
        model = TrainTimeTable
        exclude = ("id",)


class TrainTerminalFilterSerializer(serializers.Serializer):
    station_name = serializers.CharField(required=False)


class TrainTimeTableFilterSerializer(serializers.Serializer):
    station_id = serializers.CharField(required=False)
    rail_name = serializers.CharField(required=False)
    train_class = serializers.CharField(required=False)
    daily_type_code = serializers.CharField(required=False)
