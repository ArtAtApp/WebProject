# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.contrib.auth.models import User

from django.test import TestCase

from models import Artist

class ArtistTestCase(TestCase):

    def setUp(self):
        user = User("Garrosh", "ramon@gmail.com", "patata")
        artist_1 = Artist(dni="12345678C",\
            user=user, first_name="Garrosh", last_name="Hellscream",\
            phone_number=973252423, role='Artist', bank_account='471291235190')
        artist_1.save()

    def test_artist(self):
        """Artist inserted"""
        test_artist = Artist.objects.filter(user__username="Garrosh").get()
        self.assertEqual(test_artist.last_name, "Hellscream")
        pass

    #def test_average_no_review(self):
        # """The average review for a restaurant without reviews is 0"""
        # restaurant = Restaurant.objects.get(name="Unknown Restaurant")
        # self.assertEqual(restaurant.averageRating(), 0)
