from django.db import models
from django_resized import ResizedImageField


from django.contrib.auth.models import User


LANGUAGE_TYPE = [
    ('en', 'English'),
    ('cs', 'Czech'),
    ('de', 'German')]


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
        default='en')
    description = models.TextField()
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="media/books",
        force_format="WEBP",
        blank=False,
        null=False,
        )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    likes = models.ManyToManyField(
        User, related_name='book_likes', blank=True)
    user = models.ForeignKey(
        User,
        related_name='book_owner',
        on_delete=models.CASCADE
        )
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)

    class Meta:
        """ Order by title and create date """
        ordering = ['title', '-created_on']

    def __str__(self):
        string = f"{self.title} registered on {self.created_on}"
        return str(string)

    def number_of_likes(self):
        return self.likes.count()

    def get_likes(self):
        return self.likes_set.all()