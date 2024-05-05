# Generated by Django 5.0.3 on 2024-05-03 13:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_location_url_trip_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triprating',
            name='rate',
            field=models.FloatField(default=0.0, max_length=5.0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]