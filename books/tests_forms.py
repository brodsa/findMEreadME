from django.test import TestCase
from .forms import BookForm


class TestBookForm(TestCase):
    """A class to test book form"""

    def setUp(self):
        print('setup: BookForm')
        self.form = BookForm(
            {
                'title': 'Title',
                'author': 'Author',
                'published_year': 2000,
                'language': 'en'
            }
        )

    def tearDown(self):
        print('teardown: BookForm')

    def test_book_title_is_required(self):
        """Testing required book title"""
        print('Test book title to be required')

        form = BookForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_author_is_required(self):
        """Testing required author"""
        print('Test author to be required')

        form = BookForm({'author': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('author', form.errors.keys())
        self.assertEqual(form.errors['author'][0], 'This field is required.')

    def test_published_year_is_required(self):
        """Testing required published year"""
        print('Test published year to be required')

        form = BookForm({'published_year': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('published_year', form.errors.keys())
        self.assertEqual(
            form.errors['published_year'][0], 'This field is required.'
            )

    def test_language_is_required(self):
        """Testing required language"""
        print('Test language to be required')

        form = BookForm({'language': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('language', form.errors.keys())
        self.assertEqual(form.errors['language'][0], 'This field is required.')

    def test_image_book_placeholder_defaults(self):
        """Testing defaults for book image"""
        print('Test book image defaults')
        self.assertTrue(self.form.is_valid())
        self.assertEqual(
            self.form['image'].initial,
            'media/books/placeholder.placeholder.webp'
            )

    def test_image_alt_defaults(self):
        """Testing defaults for book image alt"""
        print('Test book image alt defaults')
        self.assertTrue(self.form.is_valid())
        self.assertEqual(self.form['image_alt'].initial, 'Cover image')

    def test_fields_are_explicit_in_form_metaclass(self):
        """Testing displayed fields"""
        print('Test metaclass fields')
        form = BookForm()
        print(form.Meta.fields)
        self.assertEqual(
            form.Meta.fields, (
                [
                    'title',
                    'author',
                    'published_year',
                    'language',
                    'description',
                    'image',
                    'image_alt']
                ))