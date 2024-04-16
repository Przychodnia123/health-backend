from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserModelTestCase(TestCase):
    
    def test_create_token_on_user_creation(self):
        """Test if a token is created for a new user."""
        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass"
        )
        self.assertTrue(Token.objects.filter(user=user).exists())