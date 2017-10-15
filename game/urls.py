from django.urls import reverse_lazy
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.password_validation import password_validators_help_text_html as pass_help
from . import views

app_name = 'game'
urlpatterns = [
    url(r'^$', views.game, name='index')
	]
