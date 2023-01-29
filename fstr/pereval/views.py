from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, status

# Create your views here.


class CreatePereval(generics.CreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

    def post(self, request):

        serializer_for_writing = self.serializer_class(data=request.data)
        serializer_for_writing.is_valid(raise_exception=True)
        serializer_for_writing.save()
        return Response(data={'status': status.HTTP_200_OK, 'message': 'Отправление успешно', 'id': serializer_for_writing.data['beautytitle']},
                        status=status.HTTP_200_OK)

class RetrivePatchPereval(generics.RetrieveUpdateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method RetriveNOTAllowed'})

        try:
            
        except:


        return
