from django.conf.urls import url
from . import views

app_name = 'chat'
urlpatterns = [
    url(r'^$', views.index, name='index'),  # The start point for index view
    url(r'^new-room/$', views.room_form, name='room_form')
]