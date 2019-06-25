from django.conf.urls import url
from .views import display_dashboard

urlpatterns = [
    url(r'^$', display_dashboard, name='dashboard'),
]