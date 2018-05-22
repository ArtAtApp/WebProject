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
from .forms import ArtworkForm

@login_required(login_url='/accounts/login')
def create_artwork(request):
	if request.method == "GET":
		return render(request, "create_artwork.html", {
			'form': ArtworkForm(),
			'msg': request.GET.get('msg', None),
			'type': request.GET.get('type', None),
			'artist': get_member(request.user),
			'role': get_member(request.user).role,
		})
	elif request.method == "POST":
		return post_artwork(request)

def get_artwork(request):
	"""Gets the artwork attributes extracted from the html"""

	artist = get_member(request.user)
	form = ArtworkForm(request.POST, request.FILES)
	art_type = request.POST.get('artwork_type', None)
	if form.is_valid():
		name = form.cleaned_data['name']
		price = form.cleaned_data['price']
		image = form.cleaned_data['image']

	return artist, name, art_type, price, image

def post_artwork(request):

	try:
		artist, name, art_type, price, image = get_artwork(request)
		artwork = Artwork(artist=artist, name=name, art_type=art_type,
		price=price, image=image)
		artwork.save()
		return HttpResponseRedirect(reverse('homepage'))
 	except:
		return render(request, "create_artwork.html", {
            'errors': 'Error creating artwork'
        })

# ---------- Your Artworks ----------
@login_required(login_url='/accounts/login')
def YourArtworks(request):
    if request.method == "GET":
        user = get_member(request.user)
        artwork = Artwork.objects.filter(artist=user)
        return render(request, "yourartworks.html", {
        'role': get_member(request.user).role,
        'msg': request.GET.get('msg', None),
        'type': request.GET.get('type', None),
        'artworks': artwork
        })

@login_required(login_url='/accounts/login')
def delete_artwork(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    artwork.delete()
    return HttpResponseRedirect(request.GET.get("next", "/your/artworks"))

# ---------- Modify events ----------
@login_required(login_url='/accounts/login')
def ModifyArtworks(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    if request.method == "GET":
        return render(request, "modifyartworks.html", {
        'form': ArtworkForm(),
        'event': artwork,
        'role': get_member(request.user).role,
        'msg': request.GET.get('msg', None),
        'type': request.GET.get('type', None),
        })
    elif request.method == "POST":
        return modify_data_artwork(request, artwork)


def modify_data_artwork(request, artwork):
	artist, name, art_type, price, image = get_artwork(request)
	artwork.name = name
	artwork.art_type = art_type
	artwork.price = price
	artwork.image = image
	artwork.save()
	return HttpResponseRedirect(reverse('yourartworks'))
