from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import Book


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
        'image',
    )
    prepopulated_fields = {'slug': ('title','user')}
    list_filter = ('language',)
    search_fields = ('title', 'author')



