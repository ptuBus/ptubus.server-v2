# Generated by Django 3.1.4 on 2021-03-21 15:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ptu_app_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appdb',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
