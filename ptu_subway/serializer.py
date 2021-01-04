from rest_framework import serializers
from ptu_subway.models import (
    SubwayLine,
    SubwayStation,
)


class SubwayLineSerializer(serializers.ModelSerializer):
    lineSaidName = serializers.CharField(
        allow_blank=True,
        required=False,
        allow_null=True,
    )

    class Meta:
        model = SubwayLine
        fields = "__all__"


class SubwayStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubwayStation
        fields = "__all__"
