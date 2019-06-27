from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from issue_tracker.models import Ticket, TICKET_STATUS



@login_required()
def user_profile(request):
    
    user = request.user
    
    user_tickets = [t for t in Ticket.objects.filter(created_by = user).order_by('-ticket_type', '-progress', 'status').values('name', 'id', 'status', 'progress', 'ticket_type', 'description')]
    
    ts = dict(TICKET_STATUS)
    
    for t in user_tickets:
        status = ts[t['status']]
        t['status_name'] = status
        
        if t['ticket_type'] == 'F':
            t['type_name'] = 'Feature'
        elif t['ticket_type'] == 'B':
            t['type_name'] = 'Bug'
    
    return render(request, 'profile.html', {'user': user, 'tickets': user_tickets})