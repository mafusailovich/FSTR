from rest_framework import serializers
from rest_framework.response import Response
from .models import Users, Coords, Images, PerevalAdded, PerevalImages
from django.shortcuts import redirect


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude','longitude','height']



class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['title','img']


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'name', 'fam', 'otc', 'phone']

class PerevalAddedSerializer(serializers.ModelSerializer):
    users = UsersSerializer()
    images = ImagesSerializer()
    coords = CoordsSerializer()

    class Meta:
        model = PerevalAdded
        fields = ['beautytitle','title','other_titles','connect','add_time', 'users', 'coords', 'level_winter',
        'level_spring', 'level_summer','level_autumn', 'images']


    def create(self, validated_data):
        images_data = validated_data.pop('images')
        coord_data = validated_data.pop('coords')
        users_data = validated_data.pop('users')

        if not Users.objects.filter(email=users_data['email']).exists():
            image = Images.objects.create(**images_data)
            coord = Coords.objects.create(**coord_data)
            user = Users.objects.create(**users_data)
            pereval = PerevalAdded.objects.create(user=user, coord=coord, **validated_data)
            PerevalImages.objects.create(pereval=pereval, img=image)

            return {'beautytitle': pereval.beautytitle,'title': pereval.title,'other_titles':pereval.other_titles,'connect':pereval.connect, \
                'add_time':pereval.add_time, 'users': user, 'coords': coord, 'level_winter': pereval.level_winter, \
                 'level_spring': pereval.level_spring, 'level_summer': pereval.level_summer,'level_autumn': pereval.level_autumn, 'images': image}
