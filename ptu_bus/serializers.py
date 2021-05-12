from rest_framework import serializers
from .models import BusTerminal, BusTimeTable


class BusTerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusTerminal
        exclude = ("id",)


class BusTimeTableSerializer(serializers.ModelSerializer):
    bus_terminal = BusTerminalSerializer()

    class Meta:
        model = BusTimeTable
        exclude = ("id",)
