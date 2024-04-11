from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import status

User = get_user_model()

class UserRegisterViewTestCase(APITestCase):
    
    def test_user_registration(self):
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpass",
            "password2": "testpass"
        }
        response = self.client.post("/api/healthapp/register/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['response'], 'Account has been created')