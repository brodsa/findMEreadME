from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Contact
from .forms import ContactForm


class AddContact(CreateView, SuccessMessageMixin):
    """ Send a contact message view """
    template_name = 'contact.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'Thank you for contacting us, we have received your email'
            )
        return super(AddContact, self).form_valid(form)