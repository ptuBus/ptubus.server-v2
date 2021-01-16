from django.contrib import admin
from ptu_subway.models import (
    SubwayStation,
    SubwayLine,
)


@admin.register(SubwayLine)
class SubwayLineAdmin(admin.ModelAdmin):
    fields = (
        "line_name",
        "line_code",
        "line_color_code",
        "line_said_name",
    )
    list_display = (
        "line_name",
        "line_code",
        "line_color_code",
        "line_said_name",
    )


@admin.register(SubwayStation)
class SubwayStationAdmin(admin.ModelAdmin):
    fields = (
        "station_name",
        "station_code",
        "line_code",
        "rail_line_code",
    )
    list_display = (
        "station_name",
        "station_code",
        "line_code",
        "rail_line_code",
    )
