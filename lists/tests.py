from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

'''   def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correct_html(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

        request = HttpRequest()  # (1)
        response = home_page(request)  # (2)
        html = response.content.decode('utf8')  # (3)
        #self.assertTrue(html.startswith('<html>'))  # (4)
        self.assertIn('<title>To-Do lists</title>', html)  # (5)
        #self.assertTrue(html.startswith('<!DOCTYPE html>\n<html>')) # (4)
'''