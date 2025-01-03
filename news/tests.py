from django.test import TestCase, Client
from django.utils import timezone
from .models import MoodEntry

# Create your tests here.

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('news')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('news')
        self.assertTemplateUsed(response, 'home_news.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)