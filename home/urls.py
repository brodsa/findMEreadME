from django.urls import path
from .views import Index, HowItWorks

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('how', HowItWorks.as_view(), name='how')
]