from django import forms
from .models import Ticket

class NewTicketForm(forms.ModelForm):

    name = forms.CharField(label='Name')
    description = forms.CharField(label='Description', widget=forms.Textarea)
    
    class Meta:
        model = Ticket
        fields = ['name', 'description']
