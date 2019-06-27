from django.conf.urls import url
from .views import user_profile

urlpatterns = [
    url(r'^$', user_profile, name='profile'),
]