from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserApiTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass'
        )
        # Sprawdzenie, czy token już istnieje
        try:
            self.token = Token.objects.get(user=self.user)
        except Token.DoesNotExist:
            self.token = Token.objects.create(user=self.user)

    def tearDown(self):
        # Usunięcie tokena tylko jeśli istnieje
        if hasattr(self, 'token'):
            self.token.delete()
        self.user.delete()

    def test_user_registration(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpass",
            "password2": "newpass"
        }
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['response'], 'Account has been created')

    def test_user_login(self):
        data = {
            "username": "testuser",
            "password": "testpass"
        }
        response = self.client.post(reverse("login"), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

    def test_user_logout(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = self.client.post(reverse("logout"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Message'], 'You are logged out')