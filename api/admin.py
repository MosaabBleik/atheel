from django.contrib import admin
from .models import UserInfo, City, Trip, TripRating, Favorite

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')
    #fields = ('id', 'name', 'city', 'image_tag')
    #readonly_fields = ('image_tag',)
    #readonly_fields = ('created_at',)  # Make 'created_at' read-only

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'trip')

class TripAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name', 'information')

class TripRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'rate', 'user', 'trip')
    

admin.site.register(UserInfo, ProfileAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Trip, TripAdmin)
admin.site.register(TripRating, TripRatingAdmin)