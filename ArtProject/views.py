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
		return render(request, 'login.html', {
			'errors': 'Incorrect credentials'
		})

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
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("homepage"))
    elif request.method == "GET":
        return render(request, "rolechoice.html", {
            'msg': request.GET.get('msg', None),
            'type': request.GET.get('type', None)
        })
    elif request.method == "POST":
        return render(request, "signup.html", {
            'role' : request.POST.get('role', None)
        })

def get_general_data(request):
	username = request.POST.get('usernamesignup', None)
	password = request.POST.get('passwordsignup', None)
	email = request.POST.get('emailsignup', None)
	user = User.objects.create_user(username, password, email)
	dni = request.POST.get('dnisignup', None)
	firstname = request.POST.get('firstnamesignup', None)
	lastname = request.POST.get('dnisignup', None)
	phonenumber = request.POST.get('phonenumbersignup', None)
	return user, dni, firstname, lastname, phonenumber

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
        return PostSignUp(request)

def PostSignUp(request):
	role = request.POST.get('role', None)
	if (role == 'Customer'):
		user, dni, firstname, lastname, phonenumber = get_general_data(request)
		bank_account = request.POST.get('bank_account_signup', None)
		customer = Customer(dni, user, firstname, lastname, phonenumber,\
		role, bank_account)
		customer.save()
		user.save()
		login(request, user)
		return HttpResponseRedirect(reverse('homepage'))
	elif (role == 'Artist'):
		user, dni, firstname, lastname, phonenumber = get_general_data(request)
		bank_account = request.POST.get('bank_account_signup', None)
		artist = Artist(dni, user, firstname, lastname, phonenumber,\
		role, bank_account)
		artist.save()
		user.save()
		login(request, user)
		return HttpResponseRedirect(reverse('homepage'))
	elif (role == 'Organizer'):
		user, dni, firstname, lastname, phonenumber = get_general_data(request)
		cif = request.POST.get('afiliation_CIF_signup', None)
		organizer = Organizer(dni, user, firstname, lastname, phonenumber,\
		role, cif)
		organizer.save()
		user.save()
		login(request, user)
		return HttpResponseRedirect(reverse('homepage'))

def get_general_data(request):
	username = request.POST.get('usernamesignup', None)
	password = request.POST.get('passwordsignup', None)
	email = request.POST.get('emailsignup', None)
	user = User.objects.create_user(username, password, email)
	dni = request.POST.get('dnisignup', None)
	firstname = request.POST.get('firstnamesignup', None)
	lastname = request.POST.get('dnisignup', None)
	phonenumber = request.POST.get('phonenumbersignup', None)
	return user, dni, firstname, lastname, phonenumber
