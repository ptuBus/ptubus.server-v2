from rest_framework import serializers
from .models import SchoolBusTimeTable


class SchoolBusTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolBusTimeTable
        exclude = ("id",)


class SchoolBusTimeTableFilterSerializer(serializers.Serializer):
    way = serializers.CharField(required=False)
