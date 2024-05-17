#from django.shortcuts import render
from rest_framework.views import APIView
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db.models import Avg
from .models import City, Trip, TripRating, Favorite, UserInfo
from .serializers import TripSerializer, FavoriteSerializer, CitySerializer, ProfileSerializer
from datetime import datetime
from rest_framework.permissions import AllowAny
from api.backend import EmailBackend

class Register(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        ## معلومات العميل
        username = request.data["username"]
        email = request.data["email"].lower()
        password = request.data["password"]
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        phone_number = request.data["phone_number"]

        user = User()
        user.username = username
        user.email = email
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        token = Token()
        token.user = user
        token.generate_key()
        token.save()

        profile = UserInfo()
        profile.user = user
        profile.phone_number = phone_number
        profile.save()

        return Response(status=200)


class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Required fields
        email = request.data["email"].lower()
        password = request.data["password"]

        # Authenticate user
        user = EmailBackend.authenticate(self, request, username=email, password=password)

        if user is not None:
            # Token is required to fetch data
            # and keep logged in
            token = Token.objects.get(user=user)
            login(request, user)
            data = {
                "message": "Logged in Sucessfully",
                "token": token.key,
                "login_date":datetime.today()
            }
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class Logout(APIView):
    def post(self, request):
        logout(request)
        data = {
            "message": "Logged out Sucessfully",
        }
        return Response(data=data, status=status.HTTP_200_OK)
    
    
class Profile(APIView):
    def put(self, request):
        try:
            phone_number = request.data["phone_number"]
            username = request.data["username"]
            password = request.data["password"]
            email = request.data["email"]
            first_name = request.data["first_name"]
            last_name = request.data["last_name"]
            
            user = User.objects.get(pk=request.user.pk)
            user.email = email
            user.username = username
            user.first_name = first_name
            user.last_name = last_name

            if password is not None and password != "":
                print("AAAAAAAAAAAAAAAAAAAAAAAAA")
                user.set_password(password)
            user.save()

            profile = UserInfo.objects.get(user=user)
            profile.phone_number = phone_number
            profile.save()

            return Response(status=200)

        except Exception:
            return Response(status=500)

    def get(self, request):
        user = request.user
        
        profile = UserInfo.objects.get(user=user)

        data = {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone_number": profile.phone_number
        }
        return Response(data)
    
class Trips(APIView):
    permission_classes = [AllowAny]
    def get(self, request, id=None):
        # يرجع رحلة وحدة حسب الآي دي
        if id is not None:
            if Trip.objects.filter(pk=id).exists():
                trip = Trip.objects.get(pk=id)
                average_rating = TripRating.objects.filter(trip=trip).aggregate(average_rating=Avg('rate'))['average_rating']

                serializer = TripSerializer(trip)
                data = serializer.data
                if average_rating is None:
                    data["average_rating"] = 0.0
                else:
                    data["average_rating"] = average_rating
                return Response(data)
            
            else:
                return Response(status=404)
        
        # يرجع كل الرحلات
        else:
            trips = Trip.objects.all()
            serializer = TripSerializer(trips, many=True)
            return Response({"data": serializer.data})
        
    
# class Locations(APIView):
#     permission_classes = [AllowAny]
#     def get(self, request, id=None):
        
#         if id is not None:
#             if Location.objects.filter(pk=id).exists():
#                 location = Location.objects.get(pk=id)
#                 serializer = LocationSerializer(location)
#                 return Response(serializer.data)
            
#             else:
#                 return Response(status=404)
        
#         else:
#             locations = Location.objects.all()
#             serializer = LocationSerializer(locations, many=True)
#             return Response(serializer.data)
    
    
class Favorites(APIView):
    permission_classes = [AllowAny]
    def get(self, request, id=None):
        
        if id is not None:
            if Favorite.objects.filter(pk=id).exists():
                favorite = Favorite.objects.get(pk=id)
                serializer = FavoriteSerializer(favorite)
                return Response(serializer.data)
            
            else:
                return Response(status=404)
        else:
            favorites = Favorite.objects.filter(user=request.user)
            serializer = FavoriteSerializer(favorites, many=True)
            return Response({"data": serializer.data})
        
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=401)
        
        trip_id = request.data["trip_id"]
        action = request.data["action"]

        trip = Trip.objects.get(pk=trip_id)
        if action == "add":
            if not Favorite.objects.filter(user=request.user, trip=trip).exists():

                fav = Favorite()
                fav.user = request.user
                fav.trip = trip
                fav.save()
                return Response(status=200)
            
            else:
                return Response(status=500)
        
        else:
            fav = Favorite.objects.get(trip=trip, user=request.user)
            fav.delete()
            return Response(status=200)
        
        
class Ratings(APIView):
    def post(self, request):
        trip_id = request.data["trip_id"]
        rate = request.data["rate"]
        comment = request.data["comment"]

        trip = Trip.objects.get(pk=trip_id)

        if not TripRating.objects.filter(user=request.user, trip=trip).exists():
            rating = TripRating()
            rating.trip = trip
            rating.user = request.user
            rating.comment = comment
            rating.rate = rate
            rating.save()
            return Response(status=200)
        
        else:
            return Response(status=500)

        
        
class Cities(APIView):
    permission_classes = [AllowAny]
    def get(self, request, id=None):
        if id is not None:
            if City.objects.filter(pk=id).exists():
                city = City.objects.get(pk=id)
                serializer = CitySerializer(city)
                return Response(serializer.data)
            
            else:
                Response(status=404)
    
        else:
            cities = City.objects.all()
            serializer = CitySerializer(cities, many=True)
            return Response({"data": serializer.data})