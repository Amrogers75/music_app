from django.shortcuts import render, render_to_response

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django.http import HttpResponseRedirect, HttpResponse

from main.models import Genres
from main.models import Albums, Artist, Tracks

from main.forms import UserSingUp, UserLogin

from django.contrib.auth import authenticate, login, logout
from main.models import CustomUser
from django.template import RequestContext
from django.db import IntegrityError
# Create your views here.


def signup(request):
    context = {}

    form = UserSingUp

    contex['form'] = form

    if request.method == 'POST':
        form = UserSingUp(request.POST)
        
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleand_data['email']
            password = form.cleaned_data['password']

            try:
                new_user = CustomUser.objects.create_user(email, password)
                auth_user = authenticate(email=email, password=password)
                login(request, auth_user)

                return HttpResponseRedirect('/')

            except IntergrityError, e:
                context['valid'] = "No, Because! No"
        else:
            context['valid'] = form.errors

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/')
    # return render_to_response('')


def login_view(request):
    context = {}

    form = UserLogin()

    context['form'] = form

    print "in login view"

    if request.method == 'POST':

        print "in post"
        form = UserLogin(request.POST)

        print form.errors

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            auth_user = authenticate(email=email, password=password)

            if auth_user is not None:
                login(request, auth_user)

                print "auth_user is not none"

                return HttpResponseRedirect('/')
            else:
                context['valid'] = "Please enter a User Name"

        else:
            context['valid'] = "Form is not valid."
    return render_to_response('login_view.html', context, context_instance=RequestContext(request))


class GenreListView(ListView):
    model = Genres
    template_name = 'genres_list.html'


class GenreDetailView(DetailView):
    model = Genres
    slug_field = 'genre_handle'
    template_name = 'genres_detail.html'


class GenreCreateView(CreateView):
    model = Genres
    fields = '__all__'
    template_name = 'genres_create.html'
    success_url = '/genres_list/'


class ArtistListView(ListView):
    model = Artist
    template_name = 'artist_list.html'


class ArtistDetailView(DetailView):
    model = Artist
    slug_field = 'artist_name'
    template_name = 'artist_detail.html'


class ArtistCreateView(CreateView):
    model = Artist
    fields = '__all__'
    template_name = 'artist_create.html'
    success_url = '/artist_list/'


class AlbumListView(ListView):
    model = Albums
    template_name = 'albums_list.html'


class AlbumDetailView(DetailView):
    model = Albums
    slug_field = 'album_title'
    template_name = 'albums_detail.html'


class AlbumCreateView(CreateView):
    model = Albums
    fields = '__all__'
    template_name = 'albums_create.html'
    success_url = '/albums_list/'


class TrackListView(ListView):
    model = Tracks
    template_name = 'tracks_list.html'


class TrackDetailView(DetailView):
    model = Tracks
    slug_field = 'track_id'
    template_name = 'tracks_detail.html'


# class TrackCreateView(CreateView):
#     model = Tracks
#     fields = '__all__l'
#     template_name = 'tracks_create.html'
#     success_url = '/tracks_create/'

