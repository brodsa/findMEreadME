from django.db import models


class Contact(models.Model):
    """
    A model to create contact form
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    created_on = models.DateField(auto_now_add=True)
    replied = models.BooleanField(default=False)

    class Meta:
        """ Ordering by create date """
        ordering = ['-replied', '-created_on']

    def __str__(self):
        return f"{self.name} send a message with the subject: {self.subject}"
