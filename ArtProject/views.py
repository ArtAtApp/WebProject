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
from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.

#--------- Homepage ---------
@login_required(login_url='/accounts/login')
def homepage(request):

	template = get_template("homepage.html")
	variables = {
		"version": "1.0.0.01"
	}
	output = template.render(variables)
	return HttpResponse(output)

#--------- User Login ---------
def UserLogin(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse("homepage"))
	elif request.method == "GET":
		return render(request, "login.html", {
            'msg': request.GET.get('msg', None),
            'type': request.GET.get('type', None)
        })
	elif request.method == "POST":
		return Postlogin(request)

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
	password = request.POST.get('passwordlogin', None)
	username = request.POST.get('usernamelogin', None)
	return password, username

def get_member(user):
    if Artist.objects.filter(user=user).exists():
        return Artist.objects.get(user=user)
    elif Organizer.objects.filter(user=user).exists():
        return Organizer.objects.get(user=user)
    elif Customer.objects.filter(user=user).exists():
        return Customer.objects.get(user=user)

    return None

#---------- Role choice ----------
def RoleChoice(request):
    if request.method == "GET":
        return render(request, "rolechoice.html", {
            'msg': request.GET.get('msg', None),
            'type': request.GET.get('type', None)
        })
    elif request.method == "POST":
        return render(request, "signup.html", {
            'msg': request.GET.get('msg', None),
            'type': request.GET.get('type', None)
        })

#---------- User signup ----------
def UserSignUp(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("homepage"))
    elif request.method == "GET":
        return render(request, "signup.html", {
            'msg': request.GET.get('msg', None),
            'type': request.GET.get('type', None)
        })
    elif request.method == "POST":
        return Postlogin(request)

def PostSignUp(request):
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

def get_user_signup_data(request):
	password = request.POST.get('passwordlogin', None)
	username = request.POST.get('usernamelogin', None)
	return password, username
