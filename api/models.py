from django.db import models 
from django.contrib.auth.models import User 
from django.utils.html import mark_safe 
 
 
class UserInfo(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    phone_number = models.CharField(max_length=50, null=True, blank=True) 
     
    def __str__(self): 
        return self.user.username 
     
class City(models.Model):
    name = models.CharField(max_length=200) 
    description = models.CharField(max_length=500, null=True, blank=True) 
     
    def __str__(self): 
        return self.name 
     
class Trip(models.Model): 
    site_name = models.CharField(max_length=200, null=True, blank=True)#site name 
    visitor_rating = models.CharField(max_length=500, null=True, blank=True) 
    trip_details = models.TextField(max_length=1000, null=True, blank=True) 
    historical_significance = models.CharField(max_length=500, null=True, blank=True)      
    url = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(blank=True, null=True)
     
    def __str__(self):
        return self.site_name 
     
class TripRating(models.Model): 
    comment = models.CharField(max_length=200, null=True, blank=True) 
    rate = models.FloatField(max_length=5.0, default=0.0) 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    trip = models.ForeignKey(Trip, related_name='trips', on_delete=models.CASCADE) 
 
    def __str__(self): 
        return f"{self.user.first_name} rated {self.trip.site_name} ({self.rate})"
    

class Favorite(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE) 
    def __str__(self): 
        return f"{self.user.first_name} liked {self.trip.site_name}"