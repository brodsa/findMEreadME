from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    """ Form to register Book """
    class Meta:
        """ Define model, fields, widget and labels """
        model = Book
        fields = [
            'title',
            'author',
            'published_year',
            'language',
            'description',
            'image',
            'image_alt',
        ]

        widgets = {
            "description": forms.Textarea(attrs={"cols": 3, "rows": 3}),
        }

        labels = {
            'title': 'Book Title',
            'author': 'Book Author',
            'published_year': 'Published Year',
            'language': 'Language',
            'description': 'Short Description of Book',
            'image': 'Book Cover Image',
            'image_alt': 'Describe Book Cover Image',
        }
