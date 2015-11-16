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

for album in Tracks.objects.all():

    param_dict = {'api_key': settings.FMAKEY, 'limit': 200, 'album_id': album.album_id}

    response = requests.get('http://freemusicarchive.org/api/get/albums.json', params=param_dict)

    response_dict = response.json()

    for data in response_dict['dataset']:
        print "IMAGE: %s" % data.get('album_image_file')
        print "TITLE: %s" % data.get('album_title')
        print "TRACKS: %s" % data.get('album_tracks')
        print "ARTIST: %s" % data.get('artist_id')
        print "INFORMATON: %s" % data.get('album_information')

        album, created = Albums.objects.get_or_create(album_id=data.get('album_id'))

        if data.get('album_title') != None:
            album.album_title = str(unidecode(data.get('album_title')))

        try:
            album_image = requests.get(data.get('album_image_file'))
            temp_image = NamedTemporaryFile(delete=True)
            temp_image.write(album_image.content)
            album.album_image_file = File(temp_image)
        except Exception, e:
            print e

        # try:
        #     artist, created = Artist.objects.get_or_create(artist_id=data.get("artist_id"))
        #     album.artist = artist.pk
        # except Exception, e:
        #     print e

        album.save()

    # new_album, created = Albums.objects.get_or_create(album_title=data['albums_title'])

    # new_album.album_handle = data['album_handle']
    # new_album.album_id = data['album_id']
    # new_album.album_tracks = data['album_tracks']
    # new_album.album_information = data['album_information']
    # new_album.album_image_file = data['album_image_file']
    # new_album.save()