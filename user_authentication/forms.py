from django import forms


class UserLoginForm(forms.Form):
    """Form for login in the user"""
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
