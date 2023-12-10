from django.urls import path

from .views import (
    RegisterBook,
    Books,
    BookDetail,
    DeleteBook,
    EditBook,
    BookKey,
    AddBookContribution,
    EditBookContribution,
    DeleteBookContribution,
    InsertKey
)


urlpatterns = [
    path('', RegisterBook.as_view(), name='register_book'),
    path('books/', Books.as_view(), name='books'),
    path('<slug:pk>/', BookDetail.as_view(), name='book_detail'),
    path('delete/<slug:pk>/', DeleteBook.as_view(), name='delete_book'),
    path('edit/<slug:pk>/', EditBook.as_view(), name='edit_book'),
    path('key/<slug:pk>/', BookKey.as_view(), name='book_key'),
    path(
        'new_contribution/<slug:book_id_key>/',
        AddBookContribution.as_view(),
        name='new_contribution'
        ),
    path(
        'change_contribution/<slug:slug>/',
        EditBookContribution.as_view(),
        name='change_contribution'
        ),
    path(
        'delete_contribution/<slug:pk>/',
        DeleteBookContribution.as_view(),
        name='delete_contribution'
        ),
    path('insert_key', InsertKey.as_view(), name='insert_key')
]
