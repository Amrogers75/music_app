#!/usr/bin/env python
import requests
import os, sys


sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from main.models import Tracks, Albums, Genres, Artist

for genre in Genres.objects.all():

    param_dict = {'api_key': settings.FMAKEY, 'limit': 200, 'genre_id': genre.genre_id}

    response = requests.get('http://freemusicarchive.org/api/get/genres.json', params=param_dict)
# response = requests.get("https://freemusicarchive.org/api/get/genres.json?api_key=LFXEJ6IFAB5LFWIW")

    response_dict = response.json()

for data in response_dict['dataset']:
    new_genre, created = Genres.objects.get_or_create(genre_title=data['genre_title'])

    new_genre.genre_handle = data['genre_handle']
    new_genre.genre_id = data['genre_id']
    new_genre.genre_parent_id = data["genre_parent_id"]
    new_genre.save()


    # print data['genre_title']
    # print data['genre_handle']
    # print data['genre_id']
    # print data['genre_parent_id']