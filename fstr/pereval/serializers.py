from rest_framework import serializers
from .models import Users, Coords, Images, PerevalAdded

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'name', 'fam', 'otc', 'phone']



class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude','longitude','height']



class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['title','img']


class PerevalAddedSerializer(serializers.ModelSerializer):
    users = UsersSerializer()
    coords = CoordsSerializer()
    images = ImagesSerializer()

    class Meta:
        model = PerevalAdded
        fields = ['beautytitle','title','other_titles','connect','add_time','level_winter',
        'level_spring', 'level_summer','level_autumn', 'users', 'coords', 'images']
        
