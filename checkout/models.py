from django.db import models
from issue_tracker.models import Ticket

# Create your models here.

class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    ticket = models.ForeignKey(Ticket, null=False)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)