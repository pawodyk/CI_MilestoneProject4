from django.test import TestCase
from django.apps import apps
from django.contrib.auth.models import User
from datetime import datetime as dt

from issue_tracker.models import Ticket

from .apps import CheckoutConfig
from .models import Order
from .views import *


class TestCheckoutApps(TestCase):
    """Testing App"""
    def test_app_name(self):
        self.assertEqual("checkout", CheckoutConfig.name)
        self.assertEqual("checkout", apps.get_app_config("checkout").name)

class TestCheckoutModels(TestCase):
    """Test Models"""
    def test_Order_string_representatation(self):
        usr = User.objects.create_user(username="test_username", password="test_password")
        time = dt.now()
        
        ticket = Ticket(name="test ticket", description="test description", ticket_type="F", created_by=usr)
        ticket.save()
        
        order = Order(
                full_name="test name",
                phone_number="132456789",
                country="test country",
                town_or_city="test town",
                street_address1="test address 1",
                street_address2="test address 2",
                county="test county",
                date=time,
                ticket=ticket,
                amount=100,
            )
        order.save()

        self.assertEqual(str(order), "1-{}-test name".format(time))
    

class TestCheckoutViews(TestCase):
    """Testing Views"""
    
    def test_get_checkout_page(self):
        usr = User.objects.create_user(username="test_username", password="test_password")
        self.assertTrue(usr)
        
        user = self.client.login(username="test_username", password="test_password")
        
        page = self.client.get("/checkout/")
        
        attr = page.context
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")
        
        
    def test_get_checkout_has_all_the_attributes(self):
        usr = User.objects.create_user(username="test_username", password="test_password")
        self.assertTrue(usr)
        
        user = self.client.login(username="test_username", password="test_password")
        page = self.client.get("/checkout/")
        
        attr = page.context
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")
        self.assertTrue(attr['order_form'])
        self.assertTrue(attr['payment_form'])
        self.assertTrue(attr['amount_input'])
        self.assertTrue(attr['publishable'])
        

    def test_get_checkout_when_user_is_not_loged_in(self):
        page = self.client.get("/checkout/")
        
        self.assertEqual(page.status_code, 302)
        self.assertRedirects(page, "/accounts/login/?next=/checkout/")
