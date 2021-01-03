from django.db import models


class SubwayLine(models.Model):
    lineName = models.CharField(max_length=100)
    lineCode = models.CharField(max_length=100)
    lineColorCode = models.CharField(max_length=100)
    lineSaidName = models.CharField(max_length=100, null=True)

class SubwayStation(models.Model):
    stationName = models.CharField(max_length=100)
    stationCode = models.CharField(max_length=100)
    lineCode = models.CharField(max_length=100)
    railLineCode = models.CharField(max_length=100)
