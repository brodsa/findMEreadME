from django.db import models
from django_resized import ResizedImageField


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
        string = f"{self.title} published in {self.published_year}"
        return str(string)


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
    location_hidden = models.TextField(
        null=False,
        blank=False,
        placeholder='''
            Give the details about the hidden place, i.e. gps coordinates. 
            This will help the other user to find the book.'''
            )
    comment = models.TextField(
        null=True,
        blank=True,
        placeholder='''
            You can comment on the book. 
            What did you like or not like?
            Was it ease to read?
            Did you have AHA or WOW moment?'''
            )
