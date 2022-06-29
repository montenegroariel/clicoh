from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from products.models import Product

class OrderTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='ariel', password='centinela')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        Product.objects.create(id=1,name= "Campera",price= 2000.0,stock= 10)


    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_order_list(self):
        response = self.client.get('/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_detail(self):
        response = self.client.get('/orders/', kwargs={'pk':1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_create(self):
        response = self.client.post('/orders/', data={"order_details": [{"product":1,"cuantity":1}]}, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


        