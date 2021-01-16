from django.contrib import admin
from ptu_train.models import (
    TrainStation,
    TrainTimeTable,
)


@admin.register(TrainStation)
class TrainStationAdmin(admin.ModelAdmin):
    fields = (
        "start_station_name",
        "start_station_id",
        "end_station_name",
        "end_station_id",
    )
    list_display = (
        "start_station_name",
        "start_station_id",
        "end_station_name",
        "end_station_id",
    )


@admin.register(TrainTimeTable)
class TrainTimeTableAdmin(admin.ModelAdmin):
    fields = (
        "train_station",
        "rail_name",
        "train_class",
        "departure_time",
        "schedule",
        "waste_time",
        "daily_type_code",
    )
    list_display = (
        "train_station",
        "rail_name",
        "train_class",
        "departure_time",
        "schedule",
        "waste_time",
        "daily_type_code",
    )
