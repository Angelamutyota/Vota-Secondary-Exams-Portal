# Generated by Django 3.2.7 on 2021-09-09 12:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('votapp', '0003_auto_20210909_0822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='time',
            new_name='finish',
        ),
        migrations.AddField(
            model_name='timetable',
            name='start',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
