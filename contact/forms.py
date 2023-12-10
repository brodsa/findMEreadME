from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    """ Form to make contact """
    class Meta:
        """ Define model, fields, widgets and labels """
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]

        widgets = {
            "message": forms.Textarea(
                attrs={
                    "cols": 3,
                    "rows": 3,
                    "placeholder": "Please write you message here!"
                }),
        }

        labels = {
            'name': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
        }
