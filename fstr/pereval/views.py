from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

# Create your views here.

class SubmitData(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
