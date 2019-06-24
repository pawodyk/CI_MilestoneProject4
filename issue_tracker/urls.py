from django.conf.urls import url, include
from .views import view_tracker, add_ticket, upvote_ticket


urlpatterns = [
    url(r'^$', view_tracker, name='tracker'),
    url(r'^add_ticket/(?P<ticket_type>[A-Z]{1})/$', add_ticket,  name="add_ticket"),
    url(r'^upvote_ticket/(?P<ticket_id>\d+)/$', upvote_ticket, name="upvote_ticket"),
]