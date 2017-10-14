from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from . import views


app_name = "game"
urlpatterns = [
  url(r"^$", views.game, name="index")
]
