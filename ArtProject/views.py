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
from models import *
# Create your views here.

#--------- Homepage ---------
@login_required(login_url='/accounts/login')
def homepage(request):

	template = get_template("homepage.html")
	member = get_member(request.user)
	variables = {
		'role': member.role,
		'name': member.first_name,
	}
	output = template.render(variables)
	return HttpResponse(output)

def get_member(user):
    if Customer.objects.filter(user=user).exists():
        return Customer.objects.get(user=user)
    elif Artist.objects.filter(user=user).exists():
        return Artist.objects.get(user=user)
    elif Organizer.objects.filter(user=user).exists():
        return Organizer.objects.get(user=user)

    return None

#--------- User Login ---------
def UserLogin(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse("homepage"))
	elif request.method == "GET":
		return render(request, "login.html", {
            'msg': request.GET.get('msg', None),
            'type': request.GET.get('type', None),
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
		return createCustomer(request, role)

	elif (role == 'Artist'):
		return createArtist(request, role)

	elif (role == 'Organizer'):
		return createOrganizer(request, role)

def get_general_data(request):
	username = request.POST.get('usernamesignup', None)
	password = request.POST.get('passwordsignup', None)
	email = request.POST.get('emailsignup', None)
	dni = request.POST.get('dnisignup', None)
	firstname = request.POST.get('firstnamesignup', None)
	lastname = request.POST.get('dnisignup', None)
	phonenumber = request.POST.get('phonenumbersignup', None)
	return username, password, email, dni, firstname, lastname, phonenumber

def createCustomer(request, role):
	username, password, email, dni, firstname, lastname, phonenumber\
	 = get_general_data(request)
	try:
		user = User.objects.create_user(username, email, password)
		bank_account = request.POST.get('bank_account_signup', None)
		role = request.POST.get('role', None)
		customer = Customer(dni = dni, user = user, first_name = firstname,\
		last_name = lastname, phone_number = phonenumber,\
		role = role, bank_account = bank_account)
		customer.save()
		user.save()
		login(request, user)
		return HttpResponseRedirect(reverse('homepage'))
	except:
		return render(request, "signup.html", {
            'errors': 'User already exists'
        })

def createArtist(request, role):
	username, password, email, dni, firstname, lastname, phonenumber\
	 = get_general_data(request)
	try:
		user = User.objects.create_user(username, email, password)
		bank_account = request.POST.get('bank_account_signup', None)
		artist = Artist(dni = dni, user = user, first_name = firstname,\
		 last_name = lastname, phone_number = phonenumber,\
		role = role, bank_account = bank_account)
		artist.save()
		user.save()
		login(request, user)
		return HttpResponseRedirect(reverse('homepage'))
	except:
		return render(request, "signup.html", {
            'errors': 'User already exists'
        })

def createOrganizer(request, role):
	username, password, email, dni, firstname, lastname, phonenumber\
	 = get_general_data(request)
	try:
		user = User.objects.create_user(username, email, password)
		cif = request.POST.get('afiliation_CIF_signup', None)
 		organizer = Organizer(dni = dni, user = user, first_name = firstname,\
 		 last_name = lastname, phone_number = phonenumber,\
 		role = role, afiliation_CIF = cif)
 		organizer.save()
 		user.save()
 		login(request, user)
 		return HttpResponseRedirect(reverse('homepage'))
	except:
		return render(request, "signup.html", {
            'errors': 'User already exists'
        })
