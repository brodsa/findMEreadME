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
    updated_on = models.DateField(auto_now=True)
    key = models.CharField(max_length=10, default='23')

    class Meta:
        """ Order by title and create date """
        ordering = ['-created_on', 'title', ]

    def __str__(self):
        return str(self.title)

    def get_total_readers(self):
        """ Get the total number of readers using BookContribution class """
        contributions = BookContribution.objects.filter(book_id=self.id).values()
        total_contributions = contributions.count()
        return total_contributions

    def get_num_cities(self):
        """ Get the number of unique cities of the book readers """
        cities = ( 
            BookContribution
            .objects
            .filter(book_id=self.id)
            .values('city')
            .annotate(num=models.Count("city") )
        )
        num_cities = len(cities)
        return num_cities

    def get_list_cities(self):
        """ Get the list of unique cities of the book readers"""
        cities = ( 
            BookContribution
            .objects
            .filter(book_id=self.id)
            .values('city')
            .annotate(num=models.Count("city") )
        )
        cities_ls = [city['city'] for city in list(cities)]
        return cities_ls

    def get_list_comments(self):
        """ Get the list of users and their comments"""
        comments_users = (
            BookContribution
            .objects
            .select_related('user')
            .filter(book_id=self.id)
            .values('user__username','comment')
            )
        print(list(comments_users))
        comments_ls = list(comments_users)
        print(comments_ls)
        return comments_ls

    def get_list_user_book(self):
        """ Get the list of users and their books"""
        users_books = (
            BookContribution
            .objects
            .select_related('user')
            .filter(book_id=self.id)
            .values('user__id','book')
            )
        print(list(users_books))
        comments_ls = list(users_books)
        print(users_books)
        return users_books

    def clean(self):
        """ 
            Evaluate the user inputs before saving in the database.
            The year must be between 1900 and current year.
        """
        year = self.published_year if self.published_year is not None else 0
        current_year = datetime.datetime.now().year
        if int(year) > int(current_year):
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
    created_on = models.DateField(auto_now_add=True,null=True)
    updated_on = models.DateField(auto_now=True,null=True)

    class Meta:
        """ Order by title and create date """
        ordering = ['-created_on', ]
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'book'],
                name='unique_user_book_contribution',
            )
        ]

    def __str__(self):
        string = f"{self.user} contributed to {self.book}"
        return str(string)

    def clean(self):
        """ 
            Evaluate the user inputs before saving in the database:
                - there must be description of hidden place in case of 
                hidden place is chosen
                - key validation
        """

        # hidden place description
        location_con = self.location == "at a hidden place"
        location_len = len(self.location_hidden) < 5
        if location_con and location_len:
            raise ValidationError(
                "Please, provide a full description of the hidden place."
                )

        # invalid book key
        books = Book.objects.values_list('key', flat=True)
        if self.book_key not in books:
            raise ValidationError(
                "The provided book key is invalid."
            )

        # the key does not match with the book key
        provided_key = self.book_key
        true_key = Book.objects.filter(
            id=self.book_key_id).values('key')[0]["key"]
        if provided_key != true_key:
            raise ValidationError(
                "The provided key does not match with the book key."
            )

        # the title not match with book id - given url
        provided_book = self.book
        true_book = Book.objects.filter(
            id=self.book_key_id).values('title')[0]["title"]
        if str(provided_book) != true_book:
            raise ValidationError(
                "The provided book title does not match with the queried."
            )
        
        