from django.contrib import admin
from ptu_train.models import (
    TrainTerminal,
    TrainTimeTable,
)


@admin.register(TrainTerminal)
class TrainTerminalAdmin(admin.ModelAdmin):
    fields = (
        "start_terminal_name",
        "start_terminal_id",
        "end_terminal_name",
        "end_terminal_id",
    )
    list_display = (
        "start_terminal_name",
        "start_terminal_id",
        "end_terminal_name",
        "end_terminal_id",
    )


@admin.register(TrainTimeTable)
class TrainTimeTableAdmin(admin.ModelAdmin):
    fields = (
        "train_terminal",
        "rail_name",
        "train_class",
        "departure_time",
        "schedule",
        "waste_time",
        "daily_type_code",
    )
    list_display = (
        "train_terminal",
        "rail_name",
        "train_class",
        "departure_time",
        "schedule",
        "waste_time",
        "daily_type_code",
    )
