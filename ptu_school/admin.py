from django.contrib import admin
from ptu_school.models import SchoolBusTimeTable


@admin.register(SchoolBusTimeTable)
class SchoolBusTimeTableAdmin(admin.ModelAdmin):
    fields = (
        "start_station_name",
        "start_station_id",
        "end_station_name",
        "end_station_id",
        "schedule",
        "up_down_type_code",
    )
    list_display = (
        "start_station_name",
        "start_station_id",
        "end_station_name",
        "end_station_id",
        "schedule",
        "up_down_type_code",
    )
