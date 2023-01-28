from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, status

# Create your views here.

class SubmitData(generics.CreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

    def post(self, request):
        serializer_for_writing = self.serializer_class(data=request.data)
        serializer_for_writing.is_valid(raise_exception=True)
        serializer_for_writing.save()
        return Response(data=serializer_for_writing.data, status=status.HTTP_200_OK)
