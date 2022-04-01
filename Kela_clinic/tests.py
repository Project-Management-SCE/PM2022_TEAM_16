from django.test import TestCase
from django.urls import resolve, reverse
from Kela_clinic.views import *
import unittest
from django.test.client import RequestFactory



class TestUrls(unittest.TestCase):

    def test_list_url_is_resolved(self):
        url=reverse('index')
        print(resolve(url))
# Create your tests here.
