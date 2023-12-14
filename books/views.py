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

from django.contrib import messages
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.template.response import TemplateResponse
from django.db.models import Q

from .models import Book, BookContribution, InsertedKey
from .forms import BookForm, BookContributionForm, InsertedKeyFrom

from .helpers import generate_key


class Books(ListView):
    """ List Class to view all books """
    template_name = 'books/books.html'
    model = Book
    context_object_name = 'books'
    paginate_by = 8


class BooksSearch(LoginRequiredMixin, ListView):
    """ List Class to search books """
    template_name = 'books/books_search.html'
    model = Book
    context_object_name = 'books'
    paginate_by = 8

    def get_queryset(self, **kwargs):
        """ Searching books by title or author """
        query = self.request.GET.get('q')
        if query:
            books = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(author__icontains=query)
            )
        else:
            books = self.model.objects.all()
        return books


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
        """ Test user with logged user otherwise 403 """
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

    def form_valid(self, form):
        """
            Method which creates instances after valid form data were POST
            and to show message on successful form submit

        """
        form.instance.user = self.request.user
        # success_url
        item = form.save()
        self.pk = item.pk
        # generate key after posting
        form.instance.key = generate_key(self.pk)

        messages.success(
            self.request,
            'Successfully created book'
        )

        return super(RegisterBook, self).form_valid(form)

    def get_success_url(self):
        """ Set up the books/key/id as success url"""
        return reverse_lazy('book_key', kwargs={'pk': self.pk})


class DeleteBook(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete a book """
    model = Book
    success_url = '/books/books/'

    def test_func(self):
        """ Test user with logged user otherwise 403 """
        return self.request.user == self.get_object().user

    def delete(self, request, *args, **kwargs):
        """ Display toast success on form submit """

        messages.success(
            self.request,
            'Successfully deleted book'
        )
        return super().delete(request, *args, **kwargs)


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
        """
            Set up pk for the success url and show toast when form submitted
        """
        item = form.save()
        self.pk = item.pk

        messages.success(
            self.request,
            'Book edited successfully'
        )

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

    def test_func(self):
        return self.request.user == self.get_object().user

    def get_initial(self):
        # code solution:
        # https://stackoverflow.com/questions/22083218/django-how-to-pre-populate-formview-with-dynamic-non-model-data
        """
            Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()
        slug = str(self.request).split('/')[-2]
        id_book = int(slug.split('-')[0])
        book = Book.objects.get(id=id_book)
        initial['book'] = book
        initial['book_key_id'] = id_book
        return initial

    def form_valid(self, form):
        """
            Method which creates instances after valid form data were POST
            and show toast success on form submition
        """
        try:
            # post username
            form.instance.user = self.request.user
            # populate form before sending it
            item = form.save(commit=False)
            # field: book title
            slug = str(self.request).split('/')[-2]
            id_book = int(slug.split('-')[0])
            item.book = Book.objects.get(id=id_book)
            # field: book key id
            item.book_key_id = id_book
            form.instance.book_key_id = id_book
            # field: owner status
            user_owner = Book.objects.get(id=id_book).user
            if self.request.user == user_owner:
                form.instance.user_status = 'owner'
            item.save()

            messages.success(
                self.request,
                'Successfully created new contribution'
            )

            return super(AddBookContribution, self).form_valid(form)
        except IntegrityError:
            return TemplateResponse(
                self.request, 'books/new_contribution_impossible.html'
                )


class EditBookContribution(
        LoginRequiredMixin,
        UserPassesTestMixin,
        UpdateView
        ):
    """ Edit a book contribution """
    template_name = 'books/change_contribution.html'
    model = BookContribution
    form_class = BookContributionForm
    success_url = '/books/books/'

    def test_func(self):
        """ Test user with logged user otherwise 403 """
        return self.request.user == self.get_object().user

    def get_initial(self):
        # code solution:
        # https://stackoverflow.com/questions/22083218/django-how-to-pre-populate-formview-with-dynamic-non-model-data
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super().get_initial()
        slug = str(self.request).split('/')[-2]
        id_book = int(slug.split('-')[-1])
        book = BookContribution.objects.get(slug=slug).book
        initial['book'] = book
        initial['book_key_id'] = id_book
        return initial

    def form_valid(self, form):
        try:
            """
                Method which creates instances after valid form data were POST
                and show toast success on form submit
            """
            # post username
            form.instance.user = self.request.user
            # populate form before sending it
            item = form.save(commit=False)
            # field: book title
            slug = str(self.request).split('/')[-2]
            id_book = int(slug.split('-')[-1])
            book = BookContribution.objects.get(slug=slug).book
            item.book = book
            # field: book key id
            item.book_key_id = id_book
            form.instance.book_key_id = id_book
            # field: owner status
            user_owner = Book.objects.get(id=id_book).user
            if self.request.user == user_owner:
                form.instance.user_status = 'owner'
            item.save()

            messages.success(
                self.request,
                'Successfully edited contribution'
            )

            return super(EditBookContribution, self).form_valid(form)
        except IntegrityError:
            return TemplateResponse(
                self.request, 'books/new_contribution_impossible.html'
                )


class DeleteBookContribution(
        LoginRequiredMixin,
        UserPassesTestMixin,
        DeleteView
        ):
    """ Delete a book """
    model = BookContribution
    success_url = '/books/books/'

    def test_func(self):
        return self.request.user == self.get_object().user

    def delete(self, request, *args, **kwargs):
        """ Display toast success on form submit """

        messages.success(
            self.request,
            'Successfully deleted contribution'
        )
        return super().delete(request, *args, **kwargs)


class InsertKey(CreateView):
    """ Insert Book Key """
    template_name = 'books/insert_key.html'
    model = InsertedKey
    form_class = InsertedKeyFrom
    success_url = '/books/books/'
    # overwriting get_success_url containing pk
    # https://stackoverflow.com/questions/51123269/django-formview-pass-pk-in-success-url
    # https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-editing/
    pk = None

    def form_valid(self, form):
        """ Set up pk for the success url  """
        item = form.save()
        key = item.inserted_key
        book_id = key.split('-')[0]
        self.pk = book_id
        return super(InsertKey, self).form_valid(form)

    def get_success_url(self):
        """ Set up the books/id as success url"""
        return reverse_lazy('book_detail', kwargs={'pk': self.pk})
