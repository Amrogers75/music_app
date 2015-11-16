from django.contrib import admin

# Register your models here.
from main.models import Genres, Artist, Albums, Tracks

admin.site.register(Genres)
admin.site.register(Artist)
admin.site.register(Albums)
admin.site.register(Tracks)