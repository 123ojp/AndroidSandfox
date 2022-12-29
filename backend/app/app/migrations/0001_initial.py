# Generated by Django 4.0.5 on 2022-06-23 16:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APPDetail',
            fields=[
                ('app_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('md5', models.CharField(max_length=40)),
                ('size', models.IntegerField()),
                ('androidversion_name', models.CharField(max_length=40)),
                ('uuid', models.CharField(max_length=40)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]