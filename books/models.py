import datetime

from django.db import models
from django_resized import ResizedImageField
from django.core.exceptions import ValidationError


from django.contrib.auth.models import User


LANGUAGE_TYPE = [
    ('English', 'English'),
    ('Czech', 'Czech'),
    ('German', 'German')
    ]

CITY = [
    ('Vienna', 'Vienna'),
    ('Prague', 'Prague'),
    ('Dublin', 'Dublin')
    ]

LOCATION = [
    ('by a friend', 'by a friend '),
    ('at a hidden place', 'at a hidden place')
    ]

USER_STATUS = [
    ('owner', 'owner'),
    ('contributor', 'contributor')
]


class Book(models.Model):
    """
    A model to create a book profile
    """
    title = models.CharField(max_length=150, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    published_year = models.IntegerField(null=False, blank=False)
    language = models.CharField(
        max_length=10,
        choices=LANGUAGE_TYPE,
        default='English',
        blank=False)
    description = models.TextField(null=True, blank=True)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="media/books",
        force_format="WEBP",
        default='media/books/placeholder.placeholder.webp',
        blank=True
        )
    image_alt = models.CharField(
        max_length=100,
        default='Cover image',
        blank=True
        )
    likes = models.ManyToManyField(
        User, related_name='book_likes', blank=True)
    user = models.ForeignKey(
        User,
        related_name='book_owner',
        on_delete=models.CASCADE,
        null=True
        )
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)
    key = models.CharField(max_length=10, default='23')

    class Meta:
        """ Order by title and create date """
        ordering = ['-created_on', 'title', ]

    def __str__(self):
        return str(self.title)

    def __repr__(self):
        return str(self.title)

    def clean(self):
        year = self.published_year
        current_year = datetime.datetime.now().year
        if year > int(current_year):
            raise ValidationError('Invalid year.')
        elif year < 1900:
            raise ValidationError('Invalid year, please contact us if needed.')
        else:
            return year


class BookContribution(models.Model):
    """ A model to create a book contribution """
    user = models.ForeignKey(
        User,
        related_name='book_contributor',
        on_delete=models.CASCADE,
        null=True
        )
    book = models.ForeignKey(
        Book,
        related_name='book_contribution',
        on_delete=models.CASCADE,
        null=True
        )
    book_key = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    book_key_id = models.IntegerField(default=9999)
    user_status = models.CharField(
        max_length=20,
        choices=USER_STATUS,
        default='contributor',
        blank=False
        )
    city = models.CharField(
        max_length=50,
        choices=CITY,
        blank=False,
        null=False
    )
    location = models.CharField(
        max_length=20,
        choices=LOCATION,
        blank=False,
        null=False
        )
    location_hidden = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        string = f"{self.user} contributed to {self.book}"
        return str(string)

    def clean(self):
        if self.location == "at a hidden place" and len(self.location_hidden)<5:
            raise ValidationError(
                "Please, provide a full description of the hidden place"
                )

        # invalid book key
        books = Book.objects.values_list('key', flat=True)
        if self.book_key not in books:
            raise ValidationError(
                "The provided book key is invalid."
            )

        # the key does not match with the book key
        book_titles = Book.objects.filter(
            title=self.book,
            key=self.book_key).values('title')

        if self.book not in book_titles:
            raise ValidationError(
                "The provided key does not match with the book key."
            )
        