from django.test import TestCase
from django.contrib.auth.models import User
from .models import Book, BookContribution


class TestBook(TestCase):
    """
    Unit test class for book model
    """

    def setUp(self):
        print('setup: TestBook')
        self.book = Book.objects.create(
            title='Steve Jobs',
            author='Walter Isacson',
            published_year=2011,
        )

    def tearDown(self):
        print('teardown: TestBook')

    def test_language_defaults_to_english(self):
        """Testing default language"""
        print('Test default language to English')
        self.assertEqual(self.book.language, 'English')

    def test_image_defaults_to_placeholder(self):
        """Testing default image placeholder"""
        print('Test default image')
        self.assertEqual(
            self.book.image,
            'media/books/placeholder.placeholder.webp'
            )

    def test_image_alt_defaults_to_placeholder(self):
        """Testing default image alt text placeholder"""
        print("Test defaults alt image")
        self.assertEqual(
            self.book.image_alt,
            'Cover image'
        )

    def test_str_representation_of_created_book_object(self):
        """Testing string representation of book object"""
        print("Test string of book object")
        self.assertEqual(str(self.book), 'Steve Jobs published in 2011')


class TestBookContribution(TestCase):
    """ Unit test for BookContribution model """

    def setUp(self):
        print("Set Up: BookContribution")
        self.contribution = BookContribution.objects.create()

    def tearDown(self):
        print('teardown: BookContribution')

    def test_default_user_status_to_contributor(self):
        """Testing default value for user status to be contributor"""
        print("Test default value of contributor for user status")
        self.assertEqual(
            self.contribution.user_status,
            'contributor'
        )
