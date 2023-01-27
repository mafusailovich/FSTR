from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

# Create your views here.

class SubmitData(generics.CreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer
