from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book
from .forms import BookForm


class RegisterBook(LoginRequiredMixin, CreateView):
    """ Register book view """
    template_name = 'books/register_book.html'
    model = Book
    form_class = BookForm
    success_url = '/books/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RegisterBook, self).form_valid(form)
