from django.conf.urls import url, include
from .views import view_tracker, add_ticket, upvote_ticket, view_ticket, edit_ticket


urlpatterns = [
    url(r'^$', view_tracker, name='tracker'),
    url(r'^add_ticket/(?P<ticket_type>[A-Z]{1})/$', add_ticket,  name="add_ticket"),
    url(r'^upvote_ticket/(?P<ticket_id>\d+)/$', upvote_ticket, name="upvote_ticket"),
    url(r'^view_ticket/(?P<ticket_id>\d+)/$', view_ticket, name="view_ticket"),
    url(r'^edit_ticket/(?P<ticket_id>\d+)/$', edit_ticket, name="edit_ticket"),
    
]