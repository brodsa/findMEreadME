from django.urls import path

from .views import RegisterBook


urlpatterns = [
    path('', RegisterBook.as_view(), name='register_book')
]
