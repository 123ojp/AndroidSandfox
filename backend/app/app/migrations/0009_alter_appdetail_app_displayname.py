# Generated by Django 4.0.5 on 2022-08-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_appdetail_app_displayname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdetail',
            name='app_displayname',
            field=models.CharField(default='', max_length=200),
        ),
    ]