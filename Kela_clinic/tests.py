from django.test import TestCase
from django import urls
from django.test import TestCase,SimpleTestCase
from django.urls import resolve, reverse
import unittest

# Create your tests here.
class TestUrls(unittest.TestCase):

    def test_list_url_is_resolved(self):
        url=reverse('index')
        print("HOME PAGE TEST ++++++++++++++>")
        print(resolve(url))
