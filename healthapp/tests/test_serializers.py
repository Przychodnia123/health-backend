from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from healthapp.serializers import UserRegisterSerializer

User = get_user_model()

class UserRegisterSerializerTestCase(APITestCase):
    
    def test_user_register_serializer_valid(self):
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpass",
            "password2": "testpass"
        }
        serializer = UserRegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())