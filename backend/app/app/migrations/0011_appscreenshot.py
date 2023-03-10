# Generated by Django 4.0.5 on 2022-08-08 12:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_appdetail_hook_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='APPScreenShot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=40)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('app_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.appdetail')),
            ],
        ),
    ]
