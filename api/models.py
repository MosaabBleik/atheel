from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=1000, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    position = models.CharField(max_length=200, null=True, blank=True)
    image = models.FileField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Trip(models.Model):
    title = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    information = models.CharField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class TripRating(models.Model):
    comment = models.CharField(max_length=200)
    rate = models.FloatField(max_length=5.0, default=0.0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} rated {self.trip.title} ({self.rate})"
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.first_name} liked {self.trip.title}"