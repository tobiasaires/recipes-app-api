from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'tobias@test.com'
        password = 'tobiastobias'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'tobias@TEST.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_with_invalid_email(self):
        """Test creating user with no email reaises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123423123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email='tobias@test.com',
            password='tobiastobias'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
