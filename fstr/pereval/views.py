from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import *
from rest_framework import generics, status, viewsets
from django.forms.models import model_to_dict


# Create your views here.


class CreatePereval(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

    def create(self, request):
        serializer_for_writing =  self.serializer_class(data=request.data)
        serializer_for_writing.is_valid(raise_exception=True)
        serializer_for_writing.save()
        return Response(data={'status': status.HTTP_200_OK, 'message': 'Отправление успешно', 'id': serializer_for_writing.data['beautytitle']},
                        status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        pereval = self.get_object() #получаем объект из запроса
        images = PerevalImages.objects.filter(pereval=pereval) #получаем список ссылок на изображения для перевала

        images = [model_to_dict(i.img, fields=['title','img']) for i in images] #геренируем словарь для вывода списка изображений
        for i in images:
            i['img'] = str(i['img']) #выдаем бинарное значение из базы как строку символов
        user = model_to_dict(pereval.user, exclude=['id']) #генерируем словарь с пользователями
        coords = model_to_dict(pereval.coord, exclude=['id']) #генерируем словарь координат перевала

        data = {'beautytitle': pereval.beautytitle, 'title': pereval.title, 'status': pereval.status, 'other_titles': pereval.other_titles, 'connect': pereval.connect,
                'add_time': pereval.add_time, 'user': user,'coords': coords,'level_winter': pereval.level_winter,
                'level_spring': pereval.level_spring, 'level_summer': pereval.level_summer, 'level_autumn': pereval.level_autumn, 'images': images }


    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


        return Response(data)






#class RetrivePatchPereval(generics.RetrieveUpdateAPIView):
    #queryset = PerevalAdded.objects.all()
    #serializer_class = PerevalAddedSerializer

    #def get(self, request, *args, **kwargs):
    #    pk = kwargs.get('pk', None)
    #    if not pk:
    #        return Response({'error': 'Method RetriveNOTAllowed'})

    #    try:
    #        pereval = PerevalAdded.objects.filter(pk=pk).values()
     #       print(f'{pereval}')
     #   except:
     #       print('Ошибка')


      #  return
