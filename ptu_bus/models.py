from django.db import models


class BusTerminal(models.Model):
    start_station_name = models.CharField(
        max_length=100,
        unique=True,
    )
    start_station_id = models.CharField(max_length=100)
    end_station_name = models.CharField(max_length=100)
    end_station_id = models.CharField(max_length=100)
    is_express = models.BooleanField()

    def __str__(self):
        return f"{self.start_station_name}/{self.end_station_name}"


class BusTimeTable(models.Model):
    bus_terminal = models.ForeignKey(
        BusTerminal,
        related_name="related_bus_timetable",
        on_delete=models.CASCADE,
    )
    waste_time = models.CharField(max_length=100)
    normal_fare = models.CharField(max_length=100)
    special_fare = models.CharField(max_length=100)
    night_fare = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)
    night_schedule = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.bus_terminal.end_station_name}"
