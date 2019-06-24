from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import NewTicketForm

def view_tracker(request):
    features_list = Ticket.objects.filter(ticket_type="F")
    bugs_list = Ticket.objects.filter(ticket_type="B")
    return render(request, 'tracker.html', {"features":features_list, "bugs":bugs_list})

@login_required
def add_ticket(request, ticket_type):
    if request.method == "POST":
        
        ticket_form = NewTicketForm(request.POST)
            
        if ticket_form.is_valid():
            new_ticket = ticket_form.save(commit=False)
            new_ticket.ticket_type = str(ticket_type)
            new_ticket.created_by = request.user
            new_ticket.save()
            if ticket_type == "F":
                request.session['ticket_id'] = new_ticket.id
                return redirect('checkout') ## redirect to the payment
            
            return redirect(reverse('tracker'))
            
        
    
    else:
        ticket_form = NewTicketForm()
    
    return render(request, 'add_ticket.html', { "form" : ticket_form , "ticket_type": ticket_type })
    
@login_required
def upvote_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket.upvotes += 1
    ticket.save()
    if ticket.ticket_type == "F":
        request.session['ticket_id'] = ticket.id
        return redirect('checkout')
        
    return redirect(reverse('tracker'))



# def view_ticket(request, ticket_id):
#     return render(reverse(tick))
    