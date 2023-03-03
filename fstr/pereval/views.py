from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import *
from rest_framework import generics, status, viewsets
from django.forms.models import model_to_dict
import base64
from pathlib import Path
import json
from django.views.generic import DetailView

BASE_DIR = Path(__file__).resolve().parent.parent



# Create your views here.


class PerevalViewset(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer

    def create(self, request):
        serializer_for_writing = self.serializer_class(data=request.data)
        serializer_for_writing.is_valid(raise_exception=True)
        serializer_for_writing.save()
        return Response(data={'status': status.HTTP_201_CREATED, 'message': 'Отправление успешно', 'id': serializer_for_writing.data['beautytitle']},
                        status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        pereval = self.get_object()  # получаем объект из запроса
        # получаем список ссылок на изображения для перевала
        images = PerevalImages.objects.filter(pereval=pereval)
        for i in images:
            print(i.img.img)

        # геренируем словарь для вывода списка изображений
        images = [model_to_dict(i.img, fields=['title', 'img'])
                  for i in images]
        for i in images:
            # выдаем бинарное значение из базы как строку символов
            i['img'] = str(bytes(i['img']))

        # генерируем словарь с пользователями
        user = model_to_dict(pereval.user, exclude=['id'])
        # генерируем словарь координат перевала
        coords = model_to_dict(pereval.coord, exclude=['id'])

        data = {'beautytitle': pereval.beautytitle, 'title': pereval.title, 'status': pereval.status, 'other_titles': pereval.other_titles, 'connect': pereval.connect,
                'add_time': pereval.add_time, 'user': user, 'coords': coords, 'level_winter': pereval.level_winter,
                'level_spring': pereval.level_spring, 'level_summer': pereval.level_summer, 'level_autumn': pereval.level_autumn, 'images': images}

        return Response(data)

    def partial_update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        state = serializer.data['beautytitle']
        message = serializer.data['title']

        return Response(data={'state': state, 'message': message})

    def get_queryset(self):  # переопределяем метод для того, чтобы получить из запроса нужный параметр
        queryset = PerevalAdded.objects.all()
        user_email = self.request.query_params.get('user_email', None)
        if user_email is not None:
            queryset = Users.objects.filter(email=user_email)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if queryset:  # если запрос не пустой, то будем выводить добавленые перевалы по пользователям
            if len(queryset) == 1 and 'email' not in queryset.values()[0] or len(queryset) > 1:
                queryset = Users.objects.all()
            result_dict = {}
            for q in range(len(queryset)):
                perevals = PerevalAdded.objects.filter(
                    user__id=queryset.values()[q]['id'])
                user = model_to_dict(queryset[q], exclude=['id'])
                result_dict[user['email']] = user
                for pereval in perevals:
                    p = model_to_dict(pereval, exclude=['id', 'user', 'coord'])
                    coords = model_to_dict(pereval.coord, exclude=['id'])
                    p.update(coords=coords)
                    images = PerevalImages.objects.filter(pereval=pereval)
                    images = [model_to_dict(
                        i.img, fields=['title', 'img']) for i in images]
                    for i in images:
                        i['img'] = str(bytes(i['img']))
                    p.update(images=images)
                    pereval_n = f'{pereval.beautytitle} {pereval.title}'
                    result_dict[f'{pereval_n}'] = p
        else:
            return Response({'status': status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        return Response(data=result_dict, status=status.HTTP_200_OK)


class IMGVeiw(viewsets.ModelViewSet):
    queryset = IMGTEST.objects.all()
    serializer_class = IMGTESTSerializer


    #def create(self, request):
    #    serializer = self.serializer_class(data=request.data)
        #temp = serializer.initial_data['img']
        #temp = temp[1:-1]
        #temp = temp.encode('ascii')
        #temp = base64.b64decode(temp)
     #   serializer.is_valid(raise_exception=True)
        #serializer.validated_data['img'] = temp
      #  serializer.save()
       # print(serializer.data)
        #return Response(data={'status':'ok'})

class EmpImageDisplay(DetailView):
    model = IMGTEST
    template_name = 'image_display.html'
    context_object_name = 'img'
