# Generated by Django 5.0.3 on 2024-04-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_recommendation_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='url',
        ),
        migrations.AddField(
            model_name='trip',
            name='url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]