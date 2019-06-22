from django.conf.urls import url, include
from user_authentication.views import login, logout, registration
from user_authentication import urls_pass_reset


urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^registration/$', registration, name='registration'),
    url(r'^password-reset/', include(urls_pass_reset))
]