from django.urls import path

from .views import RegisterBook, Books


urlpatterns = [
    path('', RegisterBook.as_view(), name='register_book'),
    path('books/', Books.as_view(), name='books')
]
