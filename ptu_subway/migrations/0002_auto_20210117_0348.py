# Generated by Django 3.1.4 on 2021-01-16 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ptu_subway', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subwayline',
            old_name='lineCode',
            new_name='line_code',
        ),
        migrations.RenameField(
            model_name='subwayline',
            old_name='lineName',
            new_name='line_color_code',
        ),
        migrations.RenameField(
            model_name='subwayline',
            old_name='lineColorCode',
            new_name='line_name',
        ),
        migrations.RenameField(
            model_name='subwayline',
            old_name='lineSaidName',
            new_name='line_said_name',
        ),
        migrations.RenameField(
            model_name='subwaystation',
            old_name='lineCode',
            new_name='line_code',
        ),
        migrations.RenameField(
            model_name='subwaystation',
            old_name='railLineCode',
            new_name='rail_line_code',
        ),
        migrations.RenameField(
            model_name='subwaystation',
            old_name='stationCode',
            new_name='station_code',
        ),
        migrations.RenameField(
            model_name='subwaystation',
            old_name='stationName',
            new_name='station_name',
        ),
    ]
