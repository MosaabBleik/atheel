from django.urls import path
from .views import Trips, Locations, Favorite
from . import views

urlpatterns = [
    path('authenticate/register', views.Register.as_view(), name='register'),
    path('authenticate/login', views.Login.as_view(), name='login'),
    path('authenticate/logout', views.Logout.as_view(), name='logout'),

    path('trips', Trips.as_view(), name='trips'),
    path('locations', Locations.as_view(), name='locations'),
    path('favorites', Favorite.as_view(), name='favorites'),
]