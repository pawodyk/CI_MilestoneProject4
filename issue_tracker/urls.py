from django.conf.urls import url, include
from .views import view_tracker, add_ticket


urlpatterns = [
    url(r'^$', view_tracker, name='tracker'),
    url(r'^add_ticket/(?P<tt>[A-Z]{1})/$', add_ticket,  name="add_ticket")
]