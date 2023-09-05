from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import Content

class AssignedViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()

    def test_assigned_view_with_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')

        assigned_content = Content.objects.create(
            title='Assigned Content',
            file='path/to/assigned/file.txt',
            visible='public',
            tag='video',
            topics='Baby Development',
            language='English',
        )
        assigned_content.assignedUsers.add(self.user)

        response = self.client.get(reverse('users:assigned'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'users/assigned.html')

        self.assertIn(assigned_content, response.context['allcontent'])

    def test_assigned_view_with_unauthenticated_user(self): 
        response = self.client.get(reverse('users:assigned'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login?next=/assigned/')


    def tearDown(self):
        self.user.delete()

class URLTestCase(TestCase):
    def test_assigned_view_url(self):
        self.client.force_login(User.objects.create_user(username='testuser', password='testpassword'))

        url = reverse('users:assigned')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
