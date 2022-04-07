from django.test import TestCase
from django.urls import resolve, reverse
from Kela_clinic.views import *
import unittest

class TestUrls(unittest.TestCase):

    def test_list_url_is_resolved(self):
        url=reverse('index')
        print(resolve(url))
