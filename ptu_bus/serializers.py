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


class BusTerminalFilterSerializer(serializers.Serializer):
    station_name = serializers.CharField(required=False)
    is_express = serializers.BooleanField(required=False)


class BusTimeTableFilterSerializer(serializers.Serializer):
    station_id = serializers.CharField(required=False)
