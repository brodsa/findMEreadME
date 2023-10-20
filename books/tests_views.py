import os
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Book


# Create your tests here.
class TestBookViews(TestCase):
    """ Test the book app pages """

    def setUp(self):
        """ Setup test """
        username = os.environ.get('ADMIN_USERNAME')
        password = os.environ.get('ADMIN_KEY')
        user_model = get_user_model()

        # Create USER
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=True
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

        # Create BOOK
        book = Book.objects.create(
            title='Steve Jobs',
            author='Walter Isaacson',
            published_year=2000,
            language='en')

    def test_register_book(self):
        """Test request and used template"""
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/register_book.html')

        
