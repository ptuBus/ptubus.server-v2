# Generated by Django 3.1.4 on 2021-02-03 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ptu_bus", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="busterminal",
            name="is_express",
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name="busterminal",
            name="start_station_name",
            field=models.CharField(max_length=100),
        ),
    ]
