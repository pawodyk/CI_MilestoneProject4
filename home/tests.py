from django.test import TestCase
from django.apps import apps

from .views import *
from .apps import HomeConfig


class TestViews(TestCase):
    """Testing Views"""
    
    def test_rendering_of_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        

class TestApps(TestCase):
    """Testing App"""

    def test_app_name(self):
        self.assertEqual("home", HomeConfig.name)
        self.assertEqual("home", apps.get_app_config("home").name)