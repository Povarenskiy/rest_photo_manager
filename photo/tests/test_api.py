import datetime

from requests.auth import HTTPBasicAuth
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase, RequestsClient, CoreAPIClient
from rest_framework import status
from photo.models import *


class TestApi(APITestCase):

    @classmethod
    def setUpTestData(self):
        self.url = 'http://127.0.0.1:8000/api'       


    def test_name_api(self):
        count_start = Names.objects.all().count()
        responce = self.client.post(f'{self.url}/name/', {'name':'Admin'}, format='json')
        count_new = Names.objects.all().count()

        self.assertEqual(responce.status_code, status.HTTP_201_CREATED)
        self.assertEqual(count_new - count_start, 1)


    def test_photo_api(self):
        
        with open("photo/tests/test_image.jpg", "rb") as image:
            image = SimpleUploadedFile("test_image.jpg", image.read(), content_type="image/jpg")
        
        new_photo = {
            "image_url": image,
            "people": [{'name': 'Admin'}],
            "country": "Test country",
            "city": "Test city",
            "date": datetime.date.today(),
            "description": "My test photo"
        }
        
        count_start = Photo.objects.all().count()

        User.objects.create_superuser('admintest', 'adminemail@test.com', 'admintest')
        self.client.login(username='admintest', password='admintest')
        
        responce = self.client.post(f'{self.url}/photo/', new_photo)
        count_new = Photo.objects.all().count()

        self.assertEqual(responce.status_code, status.HTTP_201_CREATED)
        self.assertEqual(count_new - count_start, 1)

