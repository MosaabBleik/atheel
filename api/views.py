#from django.shortcuts import render
from rest_framework.views import APIView
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import City, Location, Trip, TripRating, Favorite
from .serializers import TripSerializer, LocationSerializer
from datetime import datetime
from rest_framework.permissions import AllowAny
from api.backend import EmailBackend

class Register(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data["username"]
        email = request.data["email"].lower()
        password = request.data["password"]
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]

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
    
    
class Trips(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        # Fetch articles from database
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)
    
    
class Locations(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        # Fetch articles from database
        trips = Location.objects.all()
        serializer = LocationSerializer(trips, many=True)
        return Response(serializer.data)
    
class Favorite(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        # Fetch articles from database
        trips = Location.objects.all()
        serializer = LocationSerializer(trips, many=True)
        return Response(serializer.data)
