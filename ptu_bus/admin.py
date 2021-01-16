from django.contrib import admin
from ptu_bus.models import (
    BusTerminal,
    BusTimeTable,
)


@admin.register(BusTerminal)
class BusTerminalAdmin(admin.ModelAdmin):
    fields = (
        "start_station_name",
        "start_station_id",
        "end_station_name",
        "end_station_id",
        "is_express",
    )
    list_display = (
        "start_station_name",
        "start_station_id",
        "end_station_name",
        "end_station_id",
        "is_express",
    )


@admin.register(BusTimeTable)
class BusTimeTableAdmin(admin.ModelAdmin):
    fields = (
        "bus_terminal",
        "waste_time",
        "normal_fare",
        "special_fare",
        "night_fare",
        "schedule",
        "night_schedule",
    )
    list_display = (
        "bus_terminal",
        "waste_time",
        "normal_fare",
        "special_fare",
        "night_fare",
        "schedule",
        "night_schedule",
    )
