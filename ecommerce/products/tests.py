from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class ProductTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='ariel', password='centinela')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_product_list(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_detail(self):
        response = self.client.get('/products/', kwargs={'pk':1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_create(self):
        response = self.client.post('/products/', {"name": "Campera","price": 2000.0,"stock": 10})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
