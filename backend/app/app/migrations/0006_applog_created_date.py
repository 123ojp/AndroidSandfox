# Generated by Django 4.0.5 on 2022-07-22 21:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_appdetail_job_alive_time_appdetail_job_start_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applog',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
