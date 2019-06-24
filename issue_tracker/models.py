from django.db import models
from django.contrib.auth.models import User
import datetime

class Ticket(models.Model):
    
    TICKET_TYPES = (
        ('F', 'Feature'),
        ('B', 'Bug'),
    )
    
    TICKET_STATUS = (
        ("0", "Completed"),
        ("1", "In Progress"),
        ("2", "On Hold"),
        ("5", "Abandoned"),
    )
    
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    upvotes = models.IntegerField(default=1)
    contibutions = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    ticket_type = models.CharField(max_length=1, choices=TICKET_TYPES)
    status = models.CharField(max_length=1, default="1", choices=TICKET_STATUS)

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    
    
    def __str__(self):
        return "{0} : {1}{2}".format( self.created_date.strftime("%y/%m/%d %H:%M") , self.ticket_type, str(self.id) ) 