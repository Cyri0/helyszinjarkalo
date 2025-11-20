from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^create/?$', views.create_player, name='player-create'),
    re_path(r'^move/?$', views.move_player, name='move_player'),
]