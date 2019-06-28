from django.test import TestCase
from django.apps import apps

from .apps import GameConfig
from .views import *

class TestGamesApps(TestCase):
    """Testing App"""
    def test_app_name(self):
        self.assertEqual("games", GameConfig.name)
        self.assertEqual("games", apps.get_app_config("games").name)

class TestGamesViews(TestCase):
    """Testing Views"""
    
    def test_rendering_of_home_page(self):
        page = self.client.get("/games/brick_breaker/")
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "brick_breaker.html")

     

