from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^(?P<slug>[\w-]+)/?$', views.place_detail, name='place-detail'),
]