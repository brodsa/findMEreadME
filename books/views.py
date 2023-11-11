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

from django.utils.text import slugify

from .models import Book
from .forms import BookForm


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


class RegisterBook(LoginRequiredMixin, CreateView):
    """ Register book view """
    template_name = 'books/register_book.html'
    model = Book
    form_class = BookForm
    success_url = '/books/books/'

    def form_valid(self, form):
        """ Method which creates instances after valid form data were POST"""
        form.instance.user = self.request.user
        form.instance.slug = slugify(
            f"{self.request.POST.get('title')} {self.request.user}"
            )
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
    success_url = '/books/books/'

    def test_func(self):
        return self.request.user == self.get_object().user
