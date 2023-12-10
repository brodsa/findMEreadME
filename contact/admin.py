from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """ A class to add and customize contact on admin panel """
    list_display = (
        'name',
        'email',
        'subject',
        'created_on',
        'replied',
        'message',
    )

    list_filter = ('replied',)
    search_fields = ('name', 'email', 'subject')
