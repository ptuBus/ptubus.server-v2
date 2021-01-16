from django.db import models


class AppDB(models.Model):
    file_key = models.CharField(max_length=100)
