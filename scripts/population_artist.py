#!/usr/bin/env python
import requests
import os, sys
from unidecode import unidecode
# from PIL import Image
from StringIO import StringIO

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from main.models import Albums, Genres, Artist, Tracks

django.setup()

for artist in Albums.objects.all():

    param_dict = {'api_key': settings.FMAKEY, 'limit': 200, 'artist_id': artist.artist_id}

    response = requests.get('http://freemusicarchive.org/api/get/artists.json', params=param_dict)

    response_dict = response.json()

for data in response_dict['dataset']:

    artist, created = Artist.objects.get_or_create(artist_id=int(data.get('artist_id')))
    artist.artist_id = int(data.get('artist_id'))
    artist.artist_url = str(data.get('artist_url'))
    artist.artist_name = str(unidecode(data.get('artist_name')))

    if data.get('artist_bio') != None:
        artist.artist_bio = str(unidecode(data.get('artist_bio')))

    if data.get('artist_location') != None:
        artist.artist_location = str(unidecode(data.get('artist_location')))

    if data.get('artist_website') != None:
        artist.artist_website = str(unidecode(data.get('artist_website')))

    artist.save()