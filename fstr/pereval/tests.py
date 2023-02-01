from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status

# Create your tests here.

class PerevalTests(APITestCase):
    def test_post_pereval(self):
        url = reverse('submitData')
        data = {
            "beautytitle": "пер.",
            "title": "Перевал 9",
            "other_titles": "ХЗ",
            "connect": "",
            "add_time": "2023-01-27T00:04:00Z",
            "users": {
                "email": "test2@yandex.ru",
                "name": "epifan",
                "fam": "zalublinskiy",
                "otc": "mafusailovich",
                "phone": "888888888"
            },
            "coords": {
                "latitude": 88.77,
                "longitude": 88.98,
                "height": 21
            },
            "level_winter": "a;",
            "level_spring": "a;lsdkfj",
            "level_summer": "a;sdlkfj",
            "level_autumn": "ad;lsfkj",
            "images": [{"title": "a;sldkjf","img": "imagesss"},{"title": "111","img":"imagesss"}]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_listperevals(self):
        url = reverse('submitData')
        print(url)
        #data = {'name': 'DabApps'}
        response = self.client.get(url, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(Account.objects.count(), 1)
        #self.assertEqual(Account.objects.get().name, 'DabApps')
