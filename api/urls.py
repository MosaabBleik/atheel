from django.urls import path
from .views import Trips, Favorites, Cities, Profile
from . import views

urlpatterns = [
    path('authenticate/register', views.Register.as_view(), name='register'),
    path('authenticate/login', views.Login.as_view(), name='login'),
    path('authenticate/logout', views.Logout.as_view(), name='logout'),

    path('cities', Cities.as_view(), name='cities'),
    path('cities/<id>', Cities.as_view(), name='single_city'),

    path('trips', Trips.as_view(), name='trips'),
    path('trips/<id>', Trips.as_view(), name='single_trip'),

    # path('locations', Locations.as_view(), name='locations'),
    # path('locations/<id>', Locations.as_view(), name='single_location'),

    path('favorites', Favorites.as_view(), name='favorites'),
    path('favorites/<id>', Favorites.as_view(), name='single_favorite'),

    path('profile', Profile.as_view(), name='profile'),
    
]