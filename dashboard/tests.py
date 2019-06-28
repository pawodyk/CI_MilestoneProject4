from django.test import TestCase
from django.apps import apps
from django.contrib.auth.models import User

from .apps import DashboardConfig
from .views import *


class TestDashboardApps(TestCase):
    """Testing Apps"""
    def test_app_name(self):
        self.assertEqual("dashboard", DashboardConfig.name)
        self.assertEqual("dashboard", apps.get_app_config("dashboard").name)


class TestDashboardViews(TestCase):
    """Testing Views"""
    
    def test_get_dashboard_page(self):
        page = self.client.get("/dashboard/")
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "dashboard.html")
        
    def test_get_dashboard_insertion_of_full_status_name(self):
        usr = User.objects.create_user(username="test_username", password="test_password")
        
        self.assertTrue(usr)
        
        t = Ticket(name="test ticket 1", description="test description", ticket_type="F", created_by=usr)
        t.save()
        
        page = self.client.get("/dashboard/")
        tickets = page.context['tickets']

        self.assertNotEqual(tickets[0]['status'], "3")
        self.assertEqual(tickets[0]['status'], "Submitted")
        self.assertEqual(page.status_code, 200)