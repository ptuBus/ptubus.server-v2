from django.db import models


class SubwayLine(models.Model):
    line_name = models.CharField(
        max_length=100,
    )
    line_code = models.CharField(
        max_length=100,
    )
    line_color_code = models.CharField(
        max_length=100,
    )
    line_said_name = models.CharField(
        max_length=100,
        null=True,
    )

    def save(self, *args, **kwargs):
        if not self.line_said_name:
            self.line_said_name = self.line_name
        super(SubwayLine, self).save(*args, **kwargs)


class SubwayStation(models.Model):
    station_name = models.CharField(
        max_length=100,
    )
    station_code = models.CharField(
        max_length=100,
    )
    line_code = models.CharField(
        max_length=100,
    )
    rail_line_code = models.CharField(
        max_length=100,
    )
