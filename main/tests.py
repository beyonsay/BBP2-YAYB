from django.test import TestCase
from django.urls import reverse
from main.models import Content
from django.contrib.auth.models import User
from uuid import uuid4

class MainViewTestCase(TestCase):
    def test_main_view(self):
        response = self.client.get(reverse('main:main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/main.html')

    def setUp(self):
        self.content = Content.objects.create(
            title="Test Content",
            file="path/to/test/file",
            visible="public",
            tag="video",
            topics="Baby Development",
            language="English",
        )

    def test_content_view(self):
        url = reverse('main:content', args=[str(self.content.idContent)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('content', response.context)
        self.assertEqual(response.context['content'], self.content)

class CategoryViewTestCase(TestCase):
    def test_category_view(self):
        response = self.client.get(reverse('main:category', args=['Baby Development']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/category.html')

class TeesAndCeesViewTestCase(TestCase):
    def test_teesandcees_view(self):
        response = self.client.get(reverse('main:teesandcees'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/teesandcees.html')

class ContentModelTestCase(TestCase):
    def setUp(self):
        # Set up initial data for tests
        self.content = Content.objects.create(
            title='Test Content',
            file='path/to/test/file.txt',
            visible='public',
            tag='video',
            topics='Baby Development',
            language='English',
        )

    def test_content_creation(self):
        # Test if the content was created properly
        self.assertEqual(str(self.content), 'Test Content')

    def test_assigned_users(self):
        user1 = User.objects.create_user(username='user1', password='password')
        user2 = User.objects.create_user(username='user2', password='password')
        
        self.content.assignedUsers.add(user1, user2)

        self.assertEqual(self.content.assignedUsers.count(), 2)

    def tearDown(self):
        self.content.delete()

class URLTestCase(TestCase):
    def test_main_view_url(self):
        url = reverse('main:main') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    @classmethod
    def setUpTestData(cls):
        Content.objects.create(idContent=uuid4(), title='Test Content 1', file='path/to/file1.txt', visible='public', tag='video', topics='Baby Development', language='English')
        Content.objects.create(idContent=uuid4(), title='Test Content 2', file='path/to/file2.txt', visible='private', tag='image', topics='Baby Health', language='IsiXhosa')

    def test_content_view_url(self):
        # Fetch one of the created Content objects from the database
        valid_content = Content.objects.first()

        if valid_content:
            url = reverse('main:content', args=[valid_content.idContent])
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
        else:
            self.fail("No valid Content objects found in the database.")

    def test_category_view_url(self):
        url = reverse('main:category', args=['Baby Development']) 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_teesandcees_view_url(self):
        url = reverse('main:teesandcees')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
