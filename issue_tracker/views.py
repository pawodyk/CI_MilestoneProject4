from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ticket, TICKET_STATUS
from .forms import NewTicketForm

def view_tracker(request):
    features_list = [ f for f in Ticket.objects.filter(ticket_type="F").values('name', 'id', 'status', 'progress')]
    bugs_list = [b for b in Ticket.objects.filter(ticket_type="B").values('name', 'id', 'status', 'progress')]
    
    ts = dict(TICKET_STATUS)
    
    for feature in features_list:
        status = ts[feature['status']]
        feature['status'] = status
        
    for bug in bugs_list:
        status = ts[bug['status']]
        bug['status'] = status
    
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
            new_ticket.upvoted_by.add(request.user)
            new_ticket.save()
            if ticket_type == "F":
                request.session['ticket_id'] = new_ticket.id
                return redirect('checkout') ## redirect to the payment
            
            messages.success(request, "Ticket submitted sucessfully")
            return redirect(reverse('tracker'))
            
        
    
    else:
        ticket_form = NewTicketForm()
    
    return render(request, 'add_ticket.html', { "form" : ticket_form , "ticket_type": ticket_type })
    
@login_required
def upvote_ticket(request, ticket_id):

    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if ticket.ticket_type == "B":
        if request.user in ticket.upvoted_by.all():
            messages.info(request, "You already Reported this bug")
            return redirect(reverse('tracker'))
            
    ticket.upvoted_by.add(request.user)
    ticket.save()
    if ticket.ticket_type == "F":
        request.session['ticket_id'] = ticket.id
        return redirect('checkout')
    
    messages.success(request, "Ticket upvoted sucessfully")
    return redirect(reverse('tracker'))
    
@login_required()
def view_ticket(request, ticket_id):
    
    is_owner = False
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    
    if ticket.created_by == request.user:
        is_owner = True
        
        
    return render(request, 'view_ticket.html', {"ticket": ticket, "is_owner": is_owner})
    
    
@login_required()
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    
    if ticket.created_by == request.user:
        
        if request.method == 'POST':
            form = NewTicketForm(request.POST, instance=ticket)
            if form.is_valid():
                form.save()
                return redirect(reverse('tracker'))
        else:
            form = NewTicketForm(instance=ticket)
            return render(request, 'edit_ticket.html', {'form': form})
    
    messages.error(request, "You need to be an owner to have permissions to edit this ticket")
    return redirect(reverse('tracker'))