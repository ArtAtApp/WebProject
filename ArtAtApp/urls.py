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
from ArtProject.views import UserLogin, homepage, UserSignUp
from ArtProject.organizer_views import CreateEvent

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage, name = 'homepage'),
    url(r'^accounts/login$', UserLogin, name="login"),
    url(r'^accounts/logout$', logout, name="logout"),
    url(r'^accounts/signup$', UserSignUp, name="singup"),
    url(r'^create/event$', CreateEvent, name="createevent")
]
