# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-21 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtProject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(upload_to='artworks'),
        ),
    ]
