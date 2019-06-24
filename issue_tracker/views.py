from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import NewTicketForm

def view_tracker(request):
    features_list = Ticket.objects.filter(ticket_type="F")
    bugs_list = Ticket.objects.filter(ticket_type="B")
    return render(request, 'tracker.html', {"features":features_list, "bugs":bugs_list})

@login_required
def add_ticket(request, tt):
    if request.method == "POST":
        
        ticket_form = NewTicketForm(request.POST)
            
        if ticket_form.is_valid():
            new_ticket = ticket_form.save(commit=False)
            new_ticket.ticket_type = str(tt)
            new_ticket.created_by = request.user
            if tt == "F":
                pass
                #return redirect('payment', {"ticket" : new_ticket}) ## redirect to the payment
                
            new_ticket.save()
            
            return redirect('tracker')
            
        
    
    else:
        ticket_form = NewTicketForm()
    
    return render(request, 'add_ticket.html', { "form" : ticket_form , "tt": tt})