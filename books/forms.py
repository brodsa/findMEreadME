import datetime
from django import forms
from django.core.exceptions import ValidationError

from .models import Book, BookContribution


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
            'title': 'Title',
            'author': 'Author',
            'published_year': 'Published Year',
            'language': 'Language',
            'description': 'Description',
            'image': 'Cover Image',
            'image_alt': 'Describe cover image',
        }

    # def clean(self):
    #     year = self.cleaned_data["published_year"]
    #     current_year = datetime.datetime.now().year
    #     if year > int(current_year):
    #         raise ValidationError('Invalid year.')
    #     elif year < 1900:
    #         raise ValidationError('Invalid year, please contact us if needed.')
    #     else:
    #         return year


class BookContributionForm(forms.ModelForm):
    """ A class for Book Contribution Form to contribute """
    class Meta:
        """ Define model, fields, widget and labels """
        model = Book
        fields = [
            'city',
            'location',
            'location_hidden',
            'comment',
        ]

        widgets = {
            "location_hidden": forms.Textarea(attrs={"cols": 3, "rows": 3}),
            "comment": forms.Textarea(attrs={"cols": 3, "rows": 3}),
        }

        labels = {
            'city': 'City',
            'location': 'Where is the book?',
            'location_hidden': 'Describe the hidden place',
        }