# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import RegexValidator

# Create your models here.

class Person(models.Model):
	dni = models.CharField(blank=False, null=False, primary_key=True, unique=True, max_length=9)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(blank=False, null=False, max_length=30)
	last_name = models.CharField(blank=False, null=False, max_length=30)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
		message="Phone number must be entered in the format: '+999999999'. "
		"Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
	ROLES = (
		('Artist', 'Artist'),
		('Organizer', 'Organizer'),
		('Customer', 'Customer'),
	)
	role = models.CharField('Role', blank=False, null=False, choices=ROLES, max_length=25)

	def __str__(self):
		return u"%s" % self.dni

	def __unicode__(self):
		return u"%s" % self.dni

	class Meta:
		abstract = True


class Artist(Person):
	bank_account = models.CharField(blank=False, null=False, max_length=34)

class Organizer(Person):
	afiliation_CIF = models.CharField(blank=True, max_length=9)

class Customer(Person):
	bank_account = models.CharField(blank=False, null=False, max_length=34)

class Artwork(models.Model):
	artwork_id = models.AutoField(primary_key=True)
	artist = models.ForeignKey(Artist, related_name='edited_by', blank=False,\
	null=False, on_delete = models.CASCADE)
	name = models.CharField(blank=False, null=False, max_length=50)
	art_type = models.CharField(max_length=30)
	date = models.DateTimeField(default=date.today)
	price = models.IntegerField()
	STATES = (
		(1, 'Available'),
		(2, 'Displayed'),
		(3, 'Sold')
	)
	state = models.PositiveIntegerField(null=True, blank=True, choices=STATES)

class Event(models.Model):
	event_id = models.AutoField(primary_key=True)
	name = models.CharField(blank=False, null=False, max_length=50)
	created_by = models.ForeignKey(Organizer, on_delete = models.CASCADE)
	ini_date = models.DateTimeField()
	end_date = models.DateTimeField()
	artwork = models.ManyToManyField(Artwork, blank=True)
	Types = (
		('Painting', 'Painting'),
		('Sculpture', 'Sculpture'),
		('Photography', 'Photography'),
	)
	type = models.CharField('Type', blank=True, null=True, choices=Types, max_length=25)
