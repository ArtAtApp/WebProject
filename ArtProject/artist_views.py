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
from ArtProject.views import get_member

@login_required(login_url='/accounts/login')
def create_artwork(request):
	if request.method == "GET":
		return render(request, "create_artwork.html", {
			'msg': request.GET.get('msg', None),
			'type': request.GET.get('type', None),
			'role': get_member(request.user).role,
		})
	elif request.method == "POST":
		return post_artwork(request)

def get_artwork(request):
	"""Gets the artwork attributes extracted from the html"""

	artist = get_member(request.user)
	name = request.POST.get('artwork_name', None)
	art_type = request.POST.get('artwork_type', None)
	price = request.POST.get('artwork_price', None)

	return artist, name, art_type, price

def post_artwork(request):

	artist, name, art_type, price = get_artwork(request)

	# try:
	artwork = Artwork(artist=artist, name=name, art_type=art_type,
	price=price, state=1, image=None)
	artwork.save()

	return HttpResponseRedirect(reverse('homepage'))

	# except:
	#
	# 	return render(request, "create_artwork.html", {
    #         'errors': 'Error creating artwork'
    #     })
