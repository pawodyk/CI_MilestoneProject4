from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def login(request):
    """A view that manages the login form"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                        password=request.POST['password'])
            
            if user:
                auth.login(request=request, user=user)
                messages.success(request, "You are logged in")
                return redirect(reverse('index'))
                
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()

    return render(request, 'login.html', {'login_form': login_form})


@login_required
def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))



def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
        
    return render(request, 'registration.html', {"reg_form": registration_form})