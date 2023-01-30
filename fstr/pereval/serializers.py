from rest_framework import serializers, exceptions
from rest_framework.response import Response
from .models import Users, Coords, Images, PerevalAdded, PerevalImages
from django.shortcuts import redirect
from django.forms.models import model_to_dict



class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['title', 'img']


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'name', 'fam', 'otc', 'phone']


class PerevalAddedSerializer(serializers.ModelSerializer):
    users = UsersSerializer()
    images = ImagesSerializer(many=True)
    coords = CoordsSerializer()

    class Meta:
        model = PerevalAdded
        fields = ['beautytitle', 'title', 'other_titles', 'connect', 'add_time', 'users', 'coords', 'level_winter',
                  'level_spring', 'level_summer', 'level_autumn', 'images']


    def create(self, validated_data):
        # извлекаю вложенные словари
        images_data = validated_data.pop('images')
        coord_data = validated_data.pop('coords')
        users_data = validated_data.pop('users')

        if Users.objects.filter(email=users_data['email']).exists():
            user = Users.objects.get(email=users_data['email'])
        else:
            user = Users.objects.create(**users_data)

        coord = Coords.objects.create(**coord_data)
        pereval = PerevalAdded.objects.create(
            user=user, coord=coord, **validated_data)

        list_of_images = []  # пустой список для последующего возврата получившегося сложного объекта
        for i in images_data:  # создаются записи изображений в БД, отношения в таблице связей
            image = Images.objects.create(**i)
            PerevalImages.objects.create(pereval=pereval, img=image)
            list_of_images.append(image)

        data = {'beautytitle': pereval.pk, 'title': pereval.title, 'other_titles': pereval.other_titles, 'connect': pereval.connect,
                'add_time': pereval.add_time, 'users': user, 'coords': coord, 'level_winter': pereval.level_winter,
                'level_spring': pereval.level_spring, 'level_summer': pereval.level_summer, 'level_autumn': pereval.level_autumn, 'images': list_of_images}

        return data

    def update(self, instance, validated_data):

        if instance.status == 'new':
            images_data = validated_data.pop('images')
            coord_data = validated_data.pop('coords')
            users_data = validated_data.pop('users')

            images_data = [{**i} for i in images_data]
            images = PerevalImages.objects.filter(pereval=instance)
            images = [i.img for i in images]
            counter = 0
            for i in images:
                result = Images.objects.filter(id=i.pk).update(title=images_data[counter]['title'], img=images_data[counter]['img'])
                counter += 1

            coord_data = {**coord_data}
            coord = model_to_dict(instance.coord, fields=['latitude','longitude','height'])
            if coord != coord_data:
                try:
                    Coords.objects.filter(id=instance.coord.id).update(latitude=coord_data['latitude'], longitude=coord_data['longitude'],\
                    height=coord_data['height'])
                except Exception as e:
                    print(e)


            pereval_data = {**validated_data}
            pereval = model_to_dict(instance, exclude=['id','date_added', 'status', 'coord', 'user'])
            if pereval != pereval_data:
                PerevalAdded.objects.filter(id=instance.id).update(
                    beautytitle=pereval_data['beautytitle'],
                    title = pereval_data['title'],
                    other_titles = pereval_data['other_titles'],
                    connect = pereval_data['connect'],
                    add_time = pereval_data['add_time'],
                    level_winter = pereval_data['level_winter'],
                    level_spring = pereval_data['level_spring'],
                    level_summer = pereval_data['level_summer'],
                    level_autumn = pereval_data['level_autumn'],

                )

        images = PerevalImages.objects.filter(pereval=instance)
        images = [i.img for i in images]
        pereval = instance

        data = {'beautytitle': pereval.pk, 'title': pereval.title, 'other_titles': pereval.other_titles, 'connect': pereval.connect,
                'add_time': pereval.add_time, 'users': instance.user,'coords': instance.coord, 'level_winter': pereval.level_winter,
                'level_spring': pereval.level_spring, 'level_summer': pereval.level_summer, 'level_autumn': pereval.level_autumn, 'images': images}

        return data


