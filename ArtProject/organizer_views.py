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
