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
