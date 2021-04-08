from rest_framework.serializers import ModelSerializer

from ptu_bus.models import BusTerminal


class BusTerminalSerializer(ModelSerializer):
    class Meta:
        model = BusTerminal
        exclude = ("id",)
