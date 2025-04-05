from django.test import TestCase
from django.urls import reverse

class URLTest(TestCase):
    def test_url_exists(self):
        response = self.client.get(reverse('expense_list'))
        self.assertEqual(response.status_code, 200)
