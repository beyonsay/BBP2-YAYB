from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class URLTestCase(TestCase):
    def test_main_url(self):
        url = reverse('main:main') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_assigned_url(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(user)

        url = reverse('users:assigned')  # Assuming 'users' is the namespace for users.urls
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_android_url(self):
        url = reverse('android:test_token')  # Reversing the URL using the generated view name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_logout_url(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_admin_url(self):
        url = reverse('admin:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

