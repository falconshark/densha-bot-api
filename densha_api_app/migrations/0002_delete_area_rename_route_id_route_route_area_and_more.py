# Generated by Django 5.1.6 on 2025-02-25 07:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('densha_api_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='route_id',
            new_name='route_area',
        ),
        migrations.AddField(
            model_name='route',
            name='route_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
    ]
