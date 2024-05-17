from rest_framework import serializers
from .models import City, Trip, TripRating, UserInfo, Favorite

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        depth = 2
    average_rating = serializers.FloatField(read_only=True)
    
# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = '__all__'
#         depth = 1
    
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
        depth = 1

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripRating
        fields = '__all__'
        depth = 1

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        depth = 1

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
        depth = 1