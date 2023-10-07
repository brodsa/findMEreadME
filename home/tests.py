from django.test import TestCase

# Create your tests here.
class TestViews(TestCase):
    """ Test the homepage """
    def test_home_page(self):
        """ Test http request and view of homepage"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

