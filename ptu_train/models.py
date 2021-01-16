from django.db import models


class TrainStation(models.Model):
    start_station_name = models.CharField(max_length=100)
    start_station_id = models.CharField(max_length=100)
    end_station_name = models.CharField(max_length=100)
    end_station_id = models.CharField(max_length=100)


class TrainTimeTable(models.Model):
    train_station = models.ForeignKey(
        TrainStation,
        related_name="related_train_timetable",
        on_delete=models.CASCADE,
    )
    rail_name = models.CharField(max_length=100)
    train_class = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)
    waste_time = models.CharField(max_length=100)
    daily_type_code = models.CharField(max_length=100)
