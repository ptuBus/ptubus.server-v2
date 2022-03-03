import uuid as uuid
from django.db import models


class AppDB(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
    )
    file_key = models.CharField(max_length=100)
