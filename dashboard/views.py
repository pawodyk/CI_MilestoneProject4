from django.shortcuts import render
from issue_tracker.models import Ticket, TICKET_STATUS
from checkout.models import Order
import datetime

def display_dashboard(request):
    
    t_data =  Ticket.objects.all().values('name', 'ticket_type', 'status')
    tickets = [t for t in t_data]
    
    for ticket in tickets:
        ts = dict(TICKET_STATUS)
        status = ts[ticket['status']]
        
        ticket['status'] = status
    
    o_data = Order.objects.all().values('date', 'amount')
    orders = [{"Date" : str(o['date']), "Amount": float(o['amount'])} for o in o_data]
    
    return render(request, 'dashboard.html', {'tickets': tickets, 'orders': orders})