"""ArtAtApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from django.contrib.auth.views import logout
from ArtProject.views import UserLogin, homepage, UserSignUp, CurrentEvents
from ArtProject.artist_views import *
from django.views.static import serve
from ArtProject.views import validate_username
from ArtProject.organizer_views import CreateEvent, YourEvents, delete_event, ModifyEvent

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage, name = 'homepage'),
    url(r'^accounts/login$', UserLogin, name="login"),
    url(r'^accounts/logout$', logout, name="logout"),
    url(r'^accounts/signup$', UserSignUp, name="signup"),
    url(r'^create/artwork$', create_artwork, name="create_artwork"),
    url(r'^create/event$', CreateEvent, name="createevent"),
    url(r'^your/events$', YourEvents, name="yourevents"),
    url(r'^delete/event/(?P<pk>\d+)', delete_event, name='deleteevent'),
    url(r'^modify/event/(?P<pk>\d+)', ModifyEvent, name='modifyevent'),
    url(r'^your/artworks$', YourArtworks, name="yourartworks"),
    url(r'^delete/artwork/(?P<pk>\d+)', delete_artwork, name='deleteartworks'),
    url(r'^modify/artwork/(?P<pk>\d+)', ModifyArtworks, name='modifyartworks'),
    url(r'^ajax/validate_username/$', validate_username, name='validate_username'),
    url(r'^current/events/$', CurrentEvents, name='currentevents')

]

# For displaying images
urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, })
]
