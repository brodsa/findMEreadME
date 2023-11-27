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

from .models import Book, BookContribution
from .forms import BookForm, BookContributionForm

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


class BookKey(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """ Book Detail View to display Book Key """
    template_name = 'books/book_key.html'
    model = Book
    context_object_name = 'key'
    success_url = '/books/books/'

    def test_func(self):
        return self.request.user == self.get_object().user


class RegisterBook(LoginRequiredMixin, CreateView):
    """ Register book view """
    template_name = 'books/register_book.html'
    model = Book
    form_class = BookForm
    # overwriting get_success_url containing pk
    # https://stackoverflow.com/questions/51123269/django-formview-pass-pk-in-success-url
    # https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-editing/
    pk = None
    #success_url = '/books/books/'

    def form_valid(self, form):
        """ Method which creates instances after valid form data were POST"""
        form.instance.user = self.request.user
        # success_url
        item = form.save()
        self.pk = item.pk
        # generate key after posting
        form.instance.key = generate_key(self.pk)
        return super(RegisterBook, self).form_valid(form)

    def get_success_url(self):
        """ Set up the books/key/id as success url"""
        return reverse_lazy('book_key', kwargs={'pk': self.pk})


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


class AddBookContribution(LoginRequiredMixin, CreateView):
    """ Book Contribution Create View to add new Contribution """
    template_name = 'books/new_contribution.html'
    model = BookContribution
    form_class = BookContributionForm
    success_url = '/books/books/'
    context_object_name = 'contribution'

    def get_initial(self):
        # code solution: https://stackoverflow.com/questions/22083218/django-how-to-pre-populate-formview-with-dynamic-non-model-data
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()
        id_book = int(str(self.request).split('/')[-2])
        book = Book.objects.get(id=id_book)
        initial['book'] = book
        return initial

    def test_func(self):
        return self.request.user == self.get_object().user

    def form_valid(self,form):
        """ Method which creates instances after valid form data were POST"""
        # post username
        form.instance.user = self.request.user

        # post book title
        item = form.save(commit=False)
        id_book = int(str(self.request).split('/')[-2])
        item.book = Book.objects.get(id=id_book)
        # post owner status
        if self.request.user == self.get_object().user:
            item.user_status = 'owner'
        item.save()
        return super(AddBookContribution, self).form_valid(form)