from django.conf.urls import url
from . import views

app_name = 'game'
urlpatterns = [
    url(r'^$', views.game, name='index'),
    url(r'^GameRules/', views.gameRules, name='gameRules')
]
