from django.contrib import admin
from .models import City, Trip, Location, TripRating, Favorite

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    #readonly_fields = ('created_at',)  # Make 'created_at' read-only

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    #readonly_fields = ('created_at',)  # Make 'created_at' read-only

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'trip')
    #readonly_fields = ('created_at',)  # Make 'created_at' read-only

class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'information')
    #readonly_fields = ('created_at',)  # Make 'created_at' read-only

class TripRatingAdmin(admin.ModelAdmin):
    list_display = ('comment', 'rate', 'user', 'trip')
    #readonly_fields = ('created_at',)  # Make 'created_at' read-only

admin.site.register(City, CityAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Trip, TripAdmin)
admin.site.register(TripRating, TripRatingAdmin)