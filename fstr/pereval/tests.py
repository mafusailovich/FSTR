from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
import base64
import json
from .models import *


# Create your tests here.
class PerevalTests(APITestCase):

    

    def setUp(self):
        images = [b'12345', b'12345']
        for i in range(len(images)):
            images[i] = base64.b64encode(images[i]).decode('utf-8')
            images[i] = json.dumps(images[i])
        data = {
        "beautytitle": "пер.",
        "title": "Перевал 55",
        "other_titles": "оу",
        "connect": "ыдвлаоы",
        "add_time": "2023-02-07T09:51:32.582Z",
        "users": {
            "email": "test1@yandex.ru",
            "name": "string",
            "fam": "string",
            "otc": "string",
            "phone": "string"
        },
        "coords": {
            "latitude": "88.88",
            "longitude": "88.88",
            "height": "214"
        },
        "level_winter": "string",
        "level_spring": "string",
        "level_summer": "string",
        "level_autumn": "string",
        "images": [
            {
            "title": "string",
            "img": images[0]
            },
            {
            "title": "string",
            "img": images[1]
            }
            ]
        }
        response = self.client.post(reverse('submitData'), data, format='json')

    def test_get_listperevals(self):
        response = self.client.get(reverse('submitData'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrive(self):
        response = self.client.get(reverse('submitDataDet',args=[4]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_pereval(self):
        images = [b'12345', b'12345']
        for i in range(len(images)):
            images[i] = base64.b64encode(images[i]).decode('utf-8')
            images[i] = json.dumps(images[i])
        data = {
        "beautytitle": "пер.",
        "title": "Перевал 56",
        "other_titles": "оу",
        "connect": "ыдвлаоы",
        "add_time": "2023-02-07T09:51:32.582Z",
        "users": {
            "email": "test1@yandex.ru",
            "name": "string",
            "fam": "string",
            "otc": "string",
            "phone": "string"
        },
        "coords": {
            "latitude": "88.88",
            "longitude": "88.88",
            "height": "214"
        },
        "level_winter": "string",
        "level_spring": "string",
        "level_summer": "string",
        "level_autumn": "string",
        "images": [
            {
            "title": "string",
            "img": images[0]
            },
            {
            "title": "string",
            "img": images[1]
            }
            ]
        }
        response = self.client.post(reverse('submitData'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PerevalAdded.objects.count(), 2)
        self.assertEqual(Images.objects.count(), 4)
        self.assertEqual(Users.objects.count(), 1)
        self.assertEqual(PerevalImages.objects.count(), 4)
        self.assertEqual(Coords.objects.count(), 2)
