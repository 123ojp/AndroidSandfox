# Generated by Django 4.0.5 on 2022-08-10 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_appdetail_status_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdetail',
            name='status_msg',
            field=models.CharField(default='Allocating To Worker', max_length=200, null=True),
        ),
    ]