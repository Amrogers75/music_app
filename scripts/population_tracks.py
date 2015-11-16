#!/usr/bin/env python
import requests
import os, sys
from unidecode import unidecode
from StringIO import StringIO

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from main.models import Tracks, Albums, Genres, Artist

for genre in Genres.objects.all():

    param_dict = {'api_key': settings.FMAKEY, 'limit': 200, 'genre_id': genre.genre_id}

    response = requests.get('http://freemusicarchive.org/api/get/tracks.json', params=param_dict)


# response = requests.get("https://freemusicarchive.org/api/get/tracks.json?api_key=LFXEJ6IFAB5LFWIW&limit=200")

    response_dict = response.json()

for data in response_dict['dataset']:
    new_track, created = Tracks.objects.get_or_create(track_id=data.get('track_id'))

    new_track.track_title = data['track_title']
    new_track.track_file = data['track_file']
    # new_genre, = Genres.get['genre']
    # new_album.album = data['album']
    new_track.save()

    # track_id = models.IntegerField(primary_key=True)
    # album = models.ForeignKey('main.Albums', null=True)
    # genre = models.ForeignKey('main.Genres', null=True)
    # track_title = models.CharField(max_length=255, null=True)
    # track_file = models.FileField(upload_to="tracks")