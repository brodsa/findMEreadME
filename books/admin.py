from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import Book, BookKey


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    A Class to add and customize book on admin panel
    """
    list_display = (
        'title',
        'author',
        'published_year',
        'language',
        'description',
        'image'
    )
    
    list_filter = ('language',)
    search_fields = ('title', 'author')


@admin.register(BookKey)
class BookKeyAdmin(admin.ModelAdmin):
    """
    A Class to add and customize book key table on admin panel
    """
    list_display = (
        'key',
        'book'
    )
    
    list_filter = ('key',)
    search_fields = ('key',)
