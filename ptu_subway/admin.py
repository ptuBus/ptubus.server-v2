from django.contrib import admin
from ptu_subway.models import (
    SubwayStation,
    SubwayLine,
)


@admin.register(SubwayLine)
class SubwayLineAdmin(admin.ModelAdmin):
    fields = (
        "lineName",
        "lineCode",
        "lineColorCode",
        "lineSaidName",
    )
    list_display = (
        "id",
        "lineName",
        "lineCode",
        "lineColorCode",
        "lineSaidName",
    )


@admin.register(SubwayStation)
class SubwayStationAdmin(admin.ModelAdmin):
    fields = (
        "stationName",
        "stationCode",
        "lineCode",
        "railLineCode",
    )
    list_display = (
        "id",
        "stationName",
        "stationCode",
        "lineCode",
        "railLineCode",
    )
