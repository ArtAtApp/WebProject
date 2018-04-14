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
# Create your views here.

def homepage(request):
	template = get_template("homepage.html")
	variables = {
		"version": "1.0.0.01"
	}
	output = template.render(variables)
	return HttpResponse(output)

def UserLogin(request):
	if request.method == "GET":
		return GetLogin(request)
	elif request.method == "POST":
		return Postlogin(request)
	

def GetLogin(request):
	template = get_template("login.html")
	variables = {
		"version": "1.0.0.01"
	}
	output = template.render(variables)
	return HttpResponse(output)	

def Postlogin(request):
	password, username = get_user_login_data(request)
	try:
		user = authenticate(username=username, password=password)
		login(request, user)
		return HttpResponseRedirect(reverse("homepage"))
	except:
		context = {
			'errors': 'Incorrect credentials'
		}
		return render(request, 'UserLogin.html', context=context)


def get_user_login_data(request):
	password = request.POST.get('loginpassword', None)
	username = request.POST.get('username', None)
	return password, username