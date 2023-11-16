from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView
    )

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.urls import reverse_lazy

from .models import Book
from .forms import BookForm

from .helpers import generate_key


class Books(ListView):
    """ List Class to view all books """
    template_name = 'books/books.html'
    model = Book
    context_object_name = 'books'
    

class BookDetail(DetailView):
    """ Book Detail View to see book details """
    template_name = 'books/book_detail.html'
    model = Book
    context_object_name = 'book'

class BookKey(DetailView):
    """ Book Detail View to display Book Key """
    template_name = 'books/book_key.html'
    model = Book
    context_object_name = 'book'


class RegisterBook(LoginRequiredMixin, CreateView):
    """ Register book view """
    template_name = 'books/register_book.html'
    model = Book
    form_class = BookForm
    success_url = '/books/books/'

    def form_valid(self, form):
        """ Method which creates instances after valid form data were POST"""
        form.instance.user = self.request.user
        form.instance.key = generate_key()
        return super(RegisterBook, self).form_valid(form)


class DeleteBook(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete a book """
    model = Book
    success_url = '/books/books/'

    def test_func(self):
        return self.request.user == self.get_object().user


class EditBook(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Edit a book """
    template_name = 'books/edit_book.html'
    model = Book
    form_class = BookForm
    # overwriting get_success_url containing pk
    # https://stackoverflow.com/questions/51123269/django-formview-pass-pk-in-success-url
    # https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-editing/
    pk = None

    def test_func(self):
        return self.request.user == self.get_object().user

    def form_valid(self, form):
        """ Set up pk for the success url  """
        item = form.save()
        self.pk = item.pk
        return super(EditBook, self).form_valid(form)

    def get_success_url(self):
        """ Set up the books/id as success url"""
        return reverse_lazy('book_detail', kwargs={'pk': self.pk})