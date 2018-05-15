# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import models
from django.contrib import admin

# Register your models here.
admin.site.register(models.Person)
admin.site.register(models.Artist)
admin.site.register(models.Organizer)
admin.site.register(models.Customer)
admin.site.register(models.Artwork)
admin.site.register(models.Event)
