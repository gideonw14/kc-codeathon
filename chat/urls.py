from django.conf.urls import url
from chat.views import index

app_name = 'chat'
urlpatterns = [
    url(r'^$', index, name='index'),  # The start point for index view
]