from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker

from .models import User


class UserTests(APITestCase):

    def test_create_user(self):
        url = reverse('authentication_urls:users-list')

        body = {
            "username": "user_test",
            "first_name": "User",
            "last_name": "Test",
            "is_superuser": True,
            "is_staff": True,
            "email": "user@test.com",
            "password": "tecarch123",
            "is_active": True,
            "gender": 1
        }

        response = self.client.post(url, body, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get().email, 'user@test.com')
        self.assertEqual(User.objects.get().username, 'user_test')
