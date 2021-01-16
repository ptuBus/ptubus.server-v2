from django.db import models


class SchoolBusTimeTable(models.Model):
    start_station_name = models.CharField(max_length=100)
    start_station_id = models.CharField(max_length=100)
    end_station_name = models.CharField(max_length=100)
    end_station_id = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)
    up_down_type_code = models.CharField(max_length=20)
