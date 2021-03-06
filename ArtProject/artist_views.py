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
		return HttpResponseRedirect(reverse('currentevents'))
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

# ---------- Modify Artworks ----------
@login_required(login_url='/accounts/login')
def ModifyArtworks(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    form = ArtworkForm(initial={"name" : artwork.name, 'price' : artwork.price, 'image' : artwork.image})
    if request.method == "GET":
        return render(request, "modifyartworks.html", {
        'form': form,
        'artwork': artwork,
        'role': get_member(request.user).role,
        'msg': request.GET.get('msg', None),
        'type': request.GET.get('type', None),
        })
    elif request.method == "POST":
        return modify_data_artwork(request, artwork)


def modify_data_artwork(request, artwork):
    artist, name, art_type, price, image, delete = get_artwork_modified(request, artwork)
    artwork.name = name
    if art_type is not None:
        artwork.art_type = art_type
    artwork.price = price
    artwork.image = image
    artwork.save()
    if delete is True:
        user = get_member(request.user)
        artwork = Artwork.objects.filter(artist=user)
        return render(request, "yourartworks.html", {
        'role': get_member(request.user).role,
        'msg': request.GET.get('msg', None),
        'type': request.GET.get('type', None),
        'artworks': artwork,
        'errors': "The artwork has been deleted from the event due to the artwort type has changed"
        })
    else:
        return HttpResponseRedirect(reverse('yourartworks'))

def get_artwork_modified(request, artwork):
	"""Gets the artwork attributes extracted from the html"""
	artist = get_member(request.user)
	type = artwork.art_type
	delete = False
	form = ArtworkForm(request.POST, request.FILES, initial={"name" : artwork.name,\
	 'price' : artwork.price, 'image' : artwork.image})
	art_type = request.POST.get('artwork_type', None)
	if art_type!=type and artwork.state == 2:
		delete_artwork_from_event(request, artwork)
		delete = True
	if form.is_valid():
		name = form.cleaned_data['name']
		price = form.cleaned_data['price']
		image = form.cleaned_data['image']

	return artist, name, art_type, price, image, delete

def delete_artwork_from_event(request, artwork):
	event = Event.objects.get(artwork=artwork)
	event.artwork.remove(artwork)
	artwork.state=1
	artwork.save()
	event.save()

# ---------- Add Artwork to an Event ----------
@login_required(login_url='/accounts/login')
def addArtwork(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "GET":
        member = get_member(request.user)
        try:
            artworks = Artwork.objects.filter(artist=member, art_type=event.type, state=1)
            return render(request, "addartwork.html", {
            'artworks': artworks,
            'role': get_member(request.user).role,
            'msg': request.GET.get('msg', None),
            'type': request.GET.get('type', None),
             })
        except:
            return render(request, "addartwork.html", {
            'error': "You don't have artworks to post in this event",
            'role': get_member(request.user).role,
            'msg': request.GET.get('msg', None),
            'type': request.GET.get('type', None),
            })
    else:
        return PostAdd(request, event)

def PostAdd(request, event):
	try:
		member = get_member(request.user)
		pk = request.POST.get('artwork', None)
		artwork = Artwork.objects.get(pk=pk)
		artwork.state = 2
		event.artwork.add(artwork)
		artwork.save()
		event.save()
		return HttpResponseRedirect(reverse('currentevents'))
	except:
		artworks = Artwork.objects.filter(artist=member, art_type=event.type, state=1)
		return render(request, "addartwork.html", {
		'errors': 'Error adding the artwork',
		'artworks': artworks,
		'role': get_member(request.user).role,
		'msg': request.GET.get('msg', None),
		'type': request.GET.get('type', None),
		 })
