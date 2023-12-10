from django.urls import path

from .views import AddContact, ThankYouContact


urlpatterns = [
    path('', AddContact.as_view(), name='contact'),
    path('thank_you/', ThankYouContact.as_view(), name='thank_you'),
]
