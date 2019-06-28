from django.test import TestCase
from django.apps import apps
from django.shortcuts import reverse, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User

from .apps import UserAuthenticationConfig
from .views import *
from .forms import UserRegistrationForm

"""Testing App"""
class TestUserAuthenticationApps(TestCase):
    
    def test_user_auth_app_name(self):
        self.assertEqual("user_authentication", UserAuthenticationConfig.name)
        self.assertEqual("user_authentication", apps.get_app_config("user_authentication").name)

# class TestHomeViews(TestCase):
#     """Testing Views"""
    
#     def test_rendering_of_home_page(self):
#         page = self.client.get("/")
#         self.assertEqual(page.status_code, 200)
#         self.assertTemplateUsed(page, "index.html")

     
"""Testing Views"""
class TestUserAuthenticationViews(TestCase):
    
    
    """test login function"""
    def test_get_login_page(self):
        page = self.client.get('/accounts/login/')
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        self.assertTrue(page.context['login_form'])
        
    def test_get_login_for_loged_in_user(self):
        User.objects.create_user(username="test_username", password="test_password")
        user = self.client.login(username="test_username", password="test_password")
        
        page = self.client.get('/accounts/login/')
        
        self.assertEqual(page.status_code, 302)
        self.assertRedirects(page, reverse('index'))
        
    def test_post_login(self):
        User.objects.create_user(username="test_username", password="test_password")
        
        request = self.client.post('/accounts/login/', {'username': 'test_username', 'password':'test_password'}, follow=True)
        
        usr = auth.get_user(self.client)
        
        self.assertTrue(usr.is_authenticated())
        self.assertRedirects(request, reverse('index'))

    def test_post_login_failed(self):
        User.objects.create_user(username="test_username", password="test_password")
        
        request = self.client.post('/accounts/login/', {'username': 'test_username', 'password':'wrong_password'})
        
        usr = auth.get_user(self.client)
        
        self.assertFalse(usr.is_authenticated())
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, "login.html")
        
        
    """testing logout function"""
    def test_get_logout(self):
        User.objects.create_user(username="test_username", password="test_password")
        user = self.client.login(username="test_username", password="test_password")
        
        self.assertTrue(user)
        
        page = self.client.get('/accounts/logout/')
        
        usr = auth.get_user(self.client)
        
        self.assertFalse(usr.is_authenticated())
        self.assertRedirects(page, reverse('index'))
        
        
    """testing reqistration function"""
    def test_get_reqistration_page(self):
        page = self.client.get('/accounts/registration/')
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'registration.html')
        self.assertTrue(page.context['reg_form'])
        
        
    def test_get_registration_for_loged_in_user(self):
        User.objects.create_user(username="test_username", password="test_password")
        user = self.client.login(username="test_username", password="test_password")
        
        page = self.client.get('/accounts/registration/')
        
        self.assertEqual(page.status_code, 302)
        self.assertRedirects(page, reverse('index'))
        
        
    def test_post_registration(self):
        request = self.client.post('/accounts/registration/', {'email':'test@test.com', 'username':'test_user', 'password1': 'test_password', 'password2': 'test_password'})
        
        usr = get_object_or_404(User, username="test_user")
        
        self.assertTrue(usr)
        self.assertRedirects(request, reverse('index'))


    def test_post_registration_incorect_data_entered(self):
        request = self.client.post('/accounts/registration/', {'email':'test@test.com', 'username':'test_user', 'password1': 'test_password', 'password2': 'wrong_password'})
        
        usrs = User.objects.all()
        
        self.assertFalse(usrs)
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, "registration.html")
        
        
class TestUserAuthenticationForms(TestCase):
    
    
    """UserRegistrationForm"""
    def test_registration_with_email_already_used(self):
        User.objects.create_user(username="test_username", password="test_password", email="test@test.com")
        
        form = UserRegistrationForm({'email':'test@test.com', 'username':'test_user', 'password1': 'test_password', 'password2': 'test_password'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [u'Email address must be unique'])

    
    # def test_registration_with_missing_password_repeat_field(self):
    #     form = UserRegistrationForm({'email':'test@test.com', 'username':'test_user', 'password1': 'test_password', 'password2': ''})
    #     self.assertFalse(form.is_valid())
    #     self.assertEqual(form.errors['password2'], ['Please confirm your password'])