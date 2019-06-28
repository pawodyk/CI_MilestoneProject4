from django.test import TestCase
from django.apps import apps
from django.contrib.auth.models import User

from .apps import UserProfileConfig
from .views import *

from issue_tracker.models import Ticket


class TestGamesApps(TestCase):
    """Testing App"""
    def test_app_name(self):
        self.assertEqual("user_profile", UserProfileConfig.name)
        self.assertEqual("user_profile", apps.get_app_config("user_profile").name)

class TestGamesViews(TestCase):
    """Testing Views"""
    
    def test_get_user_profile_page(self):
        
        u = User.objects.create_user(username="test_username", password="test_password")
        self.assertTrue(u)
        
        user = self.client.login(username="test_username", password="test_password")
        
        page = self.client.get("/profile/")
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
        
    def test_get_user_profile_pass_attributes_to_template(self):
        
        u = User.objects.create_user(username="test_username", password="test_password")
        self.assertTrue(u)
        
        user = self.client.login(username="test_username", password="test_password")
        
        t = Ticket(name="test ticket", description="test description", ticket_type="B", created_by=u)
        t.save()
        
        page = self.client.get("/profile/")
        
        attr = page.context
        
        self.assertTrue(attr['user'])
        self.assertTrue(attr['tickets'])
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
        
    def test_get_user_profile_has_fullname_ticket_type_of_Bug(self):
        
        u = User.objects.create_user(username="test_username", password="test_password")
        self.assertTrue(u)
        
        user = self.client.login(username="test_username", password="test_password")
        
        t = Ticket(name="test ticket", description="test description", ticket_type="B", created_by=u)
        t.save()
        
        page = self.client.get("/profile/")
        
        tickets = list(page.context['tickets'])
        
        ticket = tickets[0]
        
        self.assertTrue(ticket['type_name'])
        self.assertEqual(ticket['type_name'], "Bug")
        
    def test_get_user_profile_has_fullname_ticket_type_of_Feature(self):
        
        u = User.objects.create_user(username="test_username", password="test_password")
        self.assertTrue(u)
        
        user = self.client.login(username="test_username", password="test_password")
        
        t = Ticket(name="test ticket", description="test description", ticket_type="F", created_by=u)
        t.save()
        
        page = self.client.get("/profile/")
        
        tickets = list(page.context['tickets'])
        
        ticket = tickets[0]
        
        self.assertTrue(ticket['type_name'])
        self.assertEqual(ticket['type_name'], "Feature")
        
    def test_get_user_profile_has_fullname_status_of_submitted(self):
        
        u = User.objects.create_user(username="test_username", password="test_password")
        self.assertTrue(u)
        
        user = self.client.login(username="test_username", password="test_password")
        
        t = Ticket(name="test ticket", description="test description", ticket_type="F", created_by=u)
        t.save()
        
        page = self.client.get("/profile/")
        
        tickets = list(page.context['tickets'])
        
        ticket = tickets[0]
        
        self.assertTrue(ticket['status_name'])
        self.assertEqual(ticket['status_name'], "Submitted")

    def test_get_user_profile_when_user_is_not_loged_in(self):
        page = self.client.get("/profile/")
        
        self.assertEqual(page.status_code, 302)
        self.assertRedirects(page, "/accounts/login/?next=/profile/")
     
