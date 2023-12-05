from django.contrib import admin
from .models import Book, BookContribution


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    A Class to add and customize book on admin panel
    """
    list_display = (
        'id',
        'title',
        'author',
        'published_year',
        'language',
        'description',
        'image',
        'key',
        'user'
    )

    list_filter = ('language',)
    search_fields = ('title', 'author')


@admin.register(BookContribution)
class BookContributionAdmin(admin.ModelAdmin):
    """ A class to add and customize book contribution on admin panel """

    list_display = (
        'id',
        'book_key',
        'book_key_id',
        'user_status',
        'user',
        'city',
        'location',
        'location_hidden',
        'comment',
        'slug',

    )

    list_filter = ('city', 'user_status', 'location')
    search_fields = ('city', 'book_key')
    prepopulated_fields = {"slug": ['user','book_key_id']}
