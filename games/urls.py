from django.conf.urls import url
from .views import render_game

urlpatterns = [
    url(r'^brick_breaker/$', render_game, name='game'),
]