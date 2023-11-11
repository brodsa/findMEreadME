import os
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Book


# Create your tests here.
class TestBookViewsLoggedUser(TestCase):
    """ 
    Test the book app pages when a user is created and logged in 
    """

    def setUp(self):
        """ Setup test """
        print("Setup: Test Book Views")
        self.username = os.environ.get('ADMIN_USERNAME')
        self.password = os.environ.get('ADMIN_KEY')
        user_model = get_user_model()

        # Create USER
        self.user = user_model.objects.create_user(
            username=self.username,
            password=self.password,
            is_superuser=True
        )

        self.logged_in = self.client.login(
            username=self.username, 
            password=self.password)
        self.assertTrue(self.logged_in)

        # Create BOOK
        self.book = Book.objects.create(
            user=self.user,
            title='Steve Jobs',
            author='Walter Isaacson',
            published_year=2000,
            language='en')

    def tearDown(self):
        print("tearDown: Test Book Views")

    def test_register_book(self):
        """ Test request and used template for registering a new book"""
        print("Testing New Book template and request")
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/register_book.html')

    def test_book_list(self):
        """ Test request and used template for Latest Book Page"""
        print("Testing Latest Book template and request")
        response = self.client.get('/books/books/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/books.html')

    def test_book_detail(self):
        """ Test request and used template for Book Detail Page"""
        print("Testing Book Detail template and request")
        response = self.client.get('/books/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_detail.html')

    def test_book_delete(self):
        """ Test Deletion when logged in"""
        print("Testing Book Deletion template and request when logged in")
        response = self.client.get('/books/edit/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/edit_book.html')

    def test_book_edit(self):
        """ Test Edit when logged in"""
        print("Testing Book Editing template and request when logged in")
        response = self.client.get('/books/edit/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/edit_book.html')


class TestBookViewsUnAuthorizedUser(TestCase):
    """ 
    Test the book app pages when a user is not authorized 

    """
    def setUp(self):
        """ Setup test """
        print("Setup: Test Book Views")
        self.username = os.environ.get('ADMIN_USERNAME')
        self.password = os.environ.get('ADMIN_KEY')
        user_model = get_user_model()

        # Create USER
        self.user = user_model.objects.create_user(
            username=self.username,
            password=self.password,
            is_superuser=True
        )
        self.client.login(
            username=self.username, 
            password=self.password)

        self.test_user = user_model.objects.create_user(
            username='Test',
            password='SayHiToTestUser' 
        )

        # Create BOOK
        self.book = Book.objects.create(
            user=self.test_user,
            title='Steve Jobs',
            author='Walter Isaacson',
            published_year=2000,
            language='en')

    def test_book_deletion_for_unauthorized_user(self):
        """
        Test request and used template for Book Deletion 
        in case of unauthorized user
        """
        print("Testing Book Deletion for unauthorized user")
        response = self.client.get('/books/delete/1/')
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, '403.html')

    def test_book_edit_for_unauthorized_user(self):
        """
        Test request and used template for Book Editing
        in case of unauthorized user
        """
        print("Testing Book Editing for unauthorized user")
        response = self.client.get('/books/edit/1/')
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, '403.html')



    

        
