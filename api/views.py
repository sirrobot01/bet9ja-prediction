from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import HomePage
from .serializers import HomePageSerializer,UserRegistrationSerializer
from rest_framework import status
from django.contrib.auth.models import User
from rest_auth.views import LoginView

# Create your views here.
class HomePageViews(generics.CreateAPIView):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer

class ViewOdds(generics.ListAPIView):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer

class UserRegistration(generics.CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = UserRegistrationSerializer
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.to_representation(instance=serializer.instance),
                        status=status.HTTP_201_CREATED)

class Login(LoginView):




