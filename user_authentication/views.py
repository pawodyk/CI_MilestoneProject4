from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import auth, messages
from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required


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

