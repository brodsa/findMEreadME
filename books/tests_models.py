from django.test import TestCase
from .models import Book


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
        print('Test default language to en')
        self.assertEqual(self.book.language, 'en')

