from django.db import models
from django.contrib.auth.models import User
import datetime

TICKET_TYPES = (
    ('F', 'Feature'),
    ('B', 'Bug'),
)
    
TICKET_STATUS = (
    ("0", "Completed"),
    ("1", "In Progress"),
    ("2", "Submitted"),
    ("3", "On Hold"),
    ("5", "Abandoned"),
)

class Ticket(models.Model):
    
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    contibutions = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    ticket_type = models.CharField(max_length=1, choices=TICKET_TYPES)
    status = models.CharField(max_length=1, default="2", choices=TICKET_STATUS)

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="author")
    upvoted_by = models.ManyToManyField(User, related_name="users")
    
    
    def __str__(self):
        return "{0} : {1}".format(self.ticket_type, str(self.id) ) 