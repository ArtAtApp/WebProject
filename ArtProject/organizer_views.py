# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from ArtProject.views import get_member
from models import *


# Create your views here.

@login_required(login_url='/accounts/login')
def CreateEvent(request):
    if request.method == "GET":
        return render(request, "createevent.html", {
            'role': get_member(request.user).role,
            'msg': request.GET.get('msg', None),
            'type': request.GET.get('type', None),
        })
    elif request.method == "POST":
        return postCreateEvent(request)

def postCreateEvent(request):
	name, ini_date, end_date, type, organizer = get_event_data(request)
	try:
		event = Event(name = name, created_by = organizer, ini_date = ini_date,\
		end_date = end_date, type = type)
		event.save()
		return HttpResponseRedirect(reverse('homepage'))
	except:
		return render(request, "createevent.html", {
            'errors': 'Error creating the event'
        })

def get_event_data(request):
	name = request.POST.get('name', None)
	ini_date = request.POST.get('ini_date', None)
	end_date = request.POST.get('end_date', None)
	type = request.POST.get('type', None)
	organizer = get_member(request.user)
	return name, ini_date, end_date, type, organizer
