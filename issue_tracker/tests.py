from django.test import TestCase
from django.apps import apps
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.messages import get_messages

from .apps import IssueTrackerConfig
from .models import Ticket
from .views import *

class TestIssueTrackerApps(TestCase):
    """Testing App"""
    def test_app_name(self):
        self.assertEqual("issue_tracker", IssueTrackerConfig.name)
        self.assertEqual("issue_tracker", apps.get_app_config("issue_tracker").name)


class TestTicketModels(TestCase):
    """Testing Models - Ticket"""
    
    ## MODEL FIELDS
    # name = models.CharField(max_length=30) 
    # description = models.CharField(max_length=1000) 
    # contibutions = models.DecimalField(default=0, max_digits=8, decimal_places=2) 
    # ticket_type = models.CharField(max_length=1, choices=TICKET_TYPES) 
    # status = models.CharField(max_length=1, default="3", choices=TICKET_STATUS) 
    # progress = models.IntegerField(default=0) 
    #
    # created_date = models.DateTimeField(auto_now_add=True) 
    # created_by = models.ForeignKey(User, related_name="author") 
    # upvoted_by = models.ManyToManyField(User, related_name="users") 
    
    def test_ticket_creation(self):
        
        u = User.objects.create_user(username="test_username", password="test_password")
        
        self.assertTrue(u)
        
        t = Ticket(name="test ticket", description="test description", ticket_type="F", created_by=u)
        t.save()
        
        self.assertEqual(t.name, "test ticket")
        self.assertEqual(t.description, "test description")
        self.assertEqual(t.ticket_type, "F")
        self.assertEqual(t.created_by.username, "test_username")
    
    
    def test_ticket_default_values(self):
        
        u = User.objects.create_user(username="test_username", password="test_password")
        
        self.assertTrue(u)
        
        t = Ticket(name="test ticket", description="test description", ticket_type="Bug", created_by=u)
        t.save()
        
        self.assertEqual(t.contibutions, 0)
        self.assertEqual(t.status, "3")
        self.assertEqual(t.progress, 0)
    
    
    def test_ticket_string_representation(self):
        u = User.objects.create_user(username="test_username", password="test_password")
        
        t_bug = Ticket(name="test", description="test", ticket_type="B", created_by=u)
        t_bug.save()
        
        t_feature = Ticket(name="test", description="test", ticket_type="F", created_by=u)
        t_feature.save()
        
        self.assertEqual(str(t_bug), "B1 : test @ 0")
        self.assertEqual(str(t_feature), "F2 : test @ 0")



"""Testing issue_tracker app's Views"""
class TestTrackerViews(TestCase):
    
    
    """Testing view_tracker"""
    def test_get_issue_tracker_page(self):
        page = self.client.get("/tracker/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "tracker.html")
        
    
    def test_get_issue_tracker_insertion_of_full_status_name_into_features(self):
        u = User.objects.create_user(username="test_username", password="test_password")
        
        self.assertTrue(u)
        
        t = Ticket(name="test ticket 1", description="test description", ticket_type="F", created_by=u)
        t.save()
        
        page = self.client.get("/tracker/")
        features = page.context['features']
        
        t_out = features[0]

        self.assertNotEqual(t_out['status'], "3")
        self.assertEqual(t_out['status'], "Submitted")

    
    def test_get_issue_tracker_insertion_of_full_status_name_into_bugs(self):
        u = User.objects.create_user(username="test_username", password="test_password")
        
        self.assertTrue(u)
        
        t = Ticket(name="test ticket 1", description="test description", ticket_type="B", created_by=u)
        t.save()
        
        page = self.client.get("/tracker/")
        bugs = page.context['bugs']
        
        t_out = bugs[0]

        self.assertNotEqual(t_out['status'], "3")
        self.assertEqual(t_out['status'], "Submitted")
        
        
    def test_get_issue_tracker_insertion_of_featured_ticket(self):
        u = User.objects.create_user(username="test_username", password="test_password")
        
        self.assertTrue(u)
        
        t = Ticket(name="test ticket 1", description="test description", ticket_type="F", created_by=u, status="0")
        t.save()
        
        page = self.client.get("/tracker/")
        featured = page.context['featured']

        self.assertTrue(featured)
        
        
        
    """Testing add_ticket"""
    def test_get_add_ticket_page(self):
        u = User.objects.create_user(username="test_username", password="test_password")
        
        self.assertTrue(u)
        
        user = self.client.login(username="test_username", password="test_password")
        
        
        page = self.client.get("/tracker/add_ticket/F/")
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "add_ticket.html")
        
        
    def test_get_add_ticket_for_not_loged_in_user(self):
        page = self.client.get("/tracker/add_ticket/F/")
        self.assertNotEqual(page.status_code, 200)
        self.assertRedirects(page, "/accounts/login/?next=/tracker/add_ticket/F/")
        
        
    def test_post_add_ticket_of_type_feature(self):
        u = User.objects.create_user(username="test_username", password="test_password")
        
        self.assertTrue(u)
        
        user = self.client.login(username="test_username", password="test_password") 
        
        response = self.client.post("/tracker/add_ticket/F/", {"name": "test ticket", "description":"test description"})
        
        t = get_object_or_404(Ticket, pk=1)
        
        self.assertEqual(t.name, "test ticket")
        self.assertRedirects(response, reverse('checkout'))
        
        
    def test_post_add_ticket_of_type_bug(self):
        u = User.objects.create_user(username="test_username", password="test_password")
        
        self.assertTrue(u)
        
        user = self.client.login(username="test_username", password="test_password") 
        
        response = self.client.post("/tracker/add_ticket/B/", {"name": "test ticket", "description":"test description"})
        
        t = get_object_or_404(Ticket, pk=1)
        
        self.assertEqual(t.name, "test ticket")
        self.assertRedirects(response, reverse('tracker'))
        
        
        
    """Testing upvote_ticket"""
    def test_post_upvote_ticket_of_type_feature(self):
        u = User.objects.create_user(username="test_username", password="test_password")
        self.assertTrue(u)
        
        t = Ticket(name="test ticket", description="test description", ticket_type="F", created_by=u)
        t.save()
        
        user = self.client.login(username="test_username", password="test_password")
        
        response = self.client.post("/tracker/upvote_ticket/1/")
        
        ticket = get_object_or_404(Ticket, pk=1)
        
        
        self.assertEqual(ticket.upvoted_by.count(), 1)
        self.assertRedirects(response, reverse('checkout'))
        
    def test_post_upvote_ticket_of_type_bug(self):
        u = User.objects.create_user(username="test_username", password="test_password")
        self.assertTrue(u)
        
        t = Ticket(name="test ticket", description="test description", ticket_type="B", created_by=u)
        t.save()
        
        user = self.client.login(username="test_username", password="test_password")
        
        response = self.client.post("/tracker/upvote_ticket/1/")
        
        ticket = get_object_or_404(Ticket, pk=1)
        
        
        self.assertEqual(ticket.upvoted_by.count(), 1)
        self.assertRedirects(response, reverse('tracker'))
        
    def test_post_upvote_ticket_of_type_bug_more_then_once(self):
        u = User.objects.create_user(username="test_username", password="test_password")
        self.assertTrue(u)
        
        t = Ticket(name="test ticket", description="test description", ticket_type="B", created_by=u)
        t.save()
        
        user = self.client.login(username="test_username", password="test_password")
        
        self.client.post("/tracker/upvote_ticket/1/") ##first upvote
        response = self.client.post("/tracker/upvote_ticket/1/", follow=True) ##second upvote
        
        ticket = get_object_or_404(Ticket, pk=1) 
        
        m = [str(item) for item in response.context['messages']]
        
        self.assertNotEqual(ticket.upvoted_by.count(), 2)
        self.assertTrue("You already Reported this bug" in m)
        self.assertRedirects(response, reverse('tracker'))
        
    def test_post_upvote_ticket_for_not_loged_in_user(self):
        u = User.objects.create_user(username="test_username", password="test_password")
        self.assertTrue(u)
        
        t = Ticket(name="test ticket", description="test description", ticket_type="B", created_by=u)
        t.save()
        
        self.client.post("/tracker/upvote_ticket/1/")
        self.client.post("/tracker/upvote_ticket/1/")
        page = self.client.post("/tracker/upvote_ticket/1/")
        
        ticket = get_object_or_404(Ticket, pk=1)
        
        self.assertNotEqual(page.status_code, 200)
        self.assertEqual(ticket.upvoted_by.count(), 0)
        self.assertRedirects(page, "/accounts/login/?next=/tracker/upvote_ticket/1/")
    
    
    """testing view_ticket"""
    def test_get_view_ticket_of_type_feature(self):
        u = User.objects.create_user(username="test_username", password="test_password")
        self.assertTrue(u)
        
        t = Ticket(name="test ticket", description="test description", ticket_type="F", created_by=u)
        t.save()
        
        user = self.client.login(username="test_username", password="test_password")
        
        page = self.client.get('/tracker/view_ticket/1/')
        
        ticket = page.context['ticket']
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'view_ticket.html')
        self.assertEqual(ticket.name, "test ticket")
        
        
    def test_get_view_ticket_of_type_bug(self):
        u1 = User.objects.create_user(username="test_username_1", password="test_password")
        self.assertTrue(u1)
        
        u2 = User.objects.create_user(username="test_username_2", password="test_password")
        self.assertTrue(u2)
        
        t = Ticket(name="test ticket", description="test description", ticket_type="B", created_by=u1)
        t.save()
        
        t.upvoted_by.add(u1)
        t.upvoted_by.add(u2)
        
        t.save()
        
        user = self.client.login(username="test_username_1", password="test_password")
        
        page = self.client.get('/tracker/view_ticket/1/')
        
        ticket = page.context['ticket']
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'view_ticket.html')
        self.assertEqual(ticket.name, "test ticket")
        self.assertEqual(ticket.contibutions, 2)
        
        
    def test_get_view_ticket_for_not_loged_in_user(self):
        u = User.objects.create_user(username="test_username", password="test_password")
        self.assertTrue(u)
        
        t = Ticket(name="test ticket", description="test description", ticket_type="F", created_by=u)
        t.save()
        
        page = self.client.get('/tracker/view_ticket/1/')
        
        self.assertNotEqual(page.status_code, 200)
        self.assertRedirects(page, "/accounts/login/?next=/tracker/view_ticket/1/")
        
        
    """testing edit_ticket"""
    def test_get_edit_ticket_page(self):
        u = User.objects.create_user(username="test_username", password="test_password")
        self.assertTrue(u)
        
        t = Ticket(name="test ticket", description="test description", ticket_type="F", created_by=u)
        t.save()
        
        user = self.client.login(username="test_username", password="test_password")
        
        page = self.client.get('/tracker/edit_ticket/1/')
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'edit_ticket.html')
        self.assertTrue(page.context['form'])


    def test_get_edit_ticket_for_not_owner(self):
        u1 = User.objects.create_user(username="test_username_1", password="test_password")
        self.assertTrue(u1)
        
        u2 = User.objects.create_user(username="test_username_2", password="test_password")
        self.assertTrue(u2)
        
        t = Ticket(name="test ticket", description="test description", ticket_type="F", created_by=u1)
        t.save()
        
        user = self.client.login(username="test_username_2", password="test_password")
        
        page = self.client.get('/tracker/edit_ticket/1/', follow=True)
        
        m = [str(item) for item in page.context['messages']]
        
        #self.assertNotEqual(page.status_code, 200)
        self.assertTrue("You need to be an owner to have permissions to edit this ticket" in m)
        self.assertRedirects(page, reverse('tracker'))
        
    def test_post_edit_ticket(self):
        u = User.objects.create_user(username="test_username", password="test_password")
        self.assertTrue(u)
        
        t = Ticket(name="test ticket", description="test description", ticket_type="F", created_by=u)
        t.save()
        
        user = self.client.login(username="test_username", password="test_password") 
        
        response = self.client.post("/tracker/edit_ticket/1/", {"name": "This is new name", "description":"And this is new description"})
        
        t = get_object_or_404(Ticket, pk=1)
        
        self.assertEqual(t.name, "This is new name")
        self.assertEqual(t.description, "And this is new description")
        self.assertRedirects(response, reverse('tracker'))
