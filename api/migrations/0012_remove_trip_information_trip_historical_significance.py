# Generated by Django 5.0.3 on 2024-05-17 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_trip_trip_rate_trip_visitor_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='information',
        ),
        migrations.AddField(
            model_name='trip',
            name='historical_significance',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
