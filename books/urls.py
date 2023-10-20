from django.urls import path

from .views import RegisterBook, Books, BookDetail


urlpatterns = [
    path('', RegisterBook.as_view(), name='register_book'),
    path('books/', Books.as_view(), name='books'),
    path('<slug:slug>/', BookDetail.as_view(), name='book_detail')
]
