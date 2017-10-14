from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from . import views

favicon_view = RedirectView.as_view(url='/static/main/content/images/favicon.ico',
                                    permanent=True)
# import ipdb; ipdb.set_trace()
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^favicon\.ico$', favicon_view),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^chat/', include('chat.urls')),
    url(r'^game/', include('game.urls')),
]
