# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.

class Person(models.Model):
	dni = models.CharField(unique=True, max_length=9)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

class Artist(Person):
	pass

class Organizer(Person):
	pass

class Customer(Person):
	pass

class Event(models.Model):
	#created_by = models.ForeignKey(Organizer, on_delete = "Cascade")
	ini_date = models.CharField(max_length=10)
	end_date = models.CharField(max_length=10)

class Artwork(models.Model):
	#artist = models.ForeignKey(Artist, on_delete = "Cascade")
	name = models.CharField(max_length=30)
	art_type = models.CharField(max_length=30)
	date = models.CharField(max_length=10)
	price = models.IntegerField()
	#exposed = models.ForeignKey(Event, on_delete = "Cascade")