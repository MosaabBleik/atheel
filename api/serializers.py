from rest_framework import serializers
from .models import City, Trip, TripRating, Location

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        depth = 2

    def validate_title(self, value):
        
        if len(value) < 5:
            raise serializers.ValidationError('Title must be at least 5 characters long.')
        return value
    
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        depth = 1

    def validate_title(self, value):
        
        if len(value) < 5:
            raise serializers.ValidationError('Title must be at least 5 characters long.')
        return value