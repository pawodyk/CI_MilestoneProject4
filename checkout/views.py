from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
import stripe

from .forms import MakePaymentForm, OrderForm, AmountInput
from .models import Order
from issue_tracker.models import Ticket 


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        amount_input =  AmountInput(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid() and amount_input.is_valid:
            
            amount = amount_input.cleaned_data['amount']
            
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.amount = amount
            
            ticket_id = request.session.get('ticket_id', None)
            ticket = get_object_or_404(Ticket, pk=ticket_id)
            ticket.contibutions += amount
            
            order.ticket = ticket
            
            ticket.save()
            order.save()
            
            try:
                customer = stripe.Charge.create(
                    amount = int(order.amount * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.success(request, "You have successfully paid")
                request.session['ticket_id'] = {}
                return redirect(reverse('tracker'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        amount_input = AmountInput()
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'amount_input': amount_input, 'publishable': settings.STRIPE_PUBLISHABLE})
                
            