from django.views.generic import TemplateView


class Index(TemplateView):
    """ Class for the index view """
    template_name = 'home/index.html'
