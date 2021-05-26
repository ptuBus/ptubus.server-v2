from django.db import models


class TrainTerminal(models.Model):
    key = models.IntegerField(
        default=None,
        editable=False,
    )
    start_terminal_name = models.CharField(max_length=100)
    start_terminal_id = models.CharField(max_length=100)
    end_terminal_name = models.CharField(max_length=100)
    end_terminal_id = models.CharField(max_length=100)

    def __str__(self):
        return self.end_terminal_name


class TrainTimeTable(models.Model):
    key = models.IntegerField(
        default=None,
        editable=False,
    )
    train_terminal = models.ForeignKey(
        TrainTerminal,
        related_name="related_train_timetable",
        on_delete=models.CASCADE,
    )
    rail_name = models.CharField(max_length=100)
    train_class = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)
    waste_time = models.CharField(max_length=100)
    daily_type_code = models.CharField(max_length=100)

    def __str__(self):
        return self.train_terminal.end_terminal_name
