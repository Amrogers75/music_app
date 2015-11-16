"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from main import views

from django.views.generic.edit import CreateView

from main.forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', views.GenreListView.as_view()),
    url(r'^genres_list/$', views.GenreListView.as_view(), name='genre_list'),
    # url(r'^genres_detail/(?P<pk>\d+)/$', views.GenreDetailView.as_view()),
    url(r'^genres_detail/(?P<slug>.+)/$', views.GenreDetailView.as_view()),
    url(r'^genres_create/$', views.GenreCreateView.as_view()),

    url(r'^albums_list/$', views.AlbumListView.as_view()),
    url(r'^albums_detail/(?P<slug>.+)/$', views.AlbumDetailView.as_view()),
    url(r'^albums_create/$', views.AlbumCreateView.as_view()),

    url(r'^artist_list/$', views.ArtistListView.as_view()),
    url(r'^artist_detail/(?P<slug>.+)/$', views.ArtistDetailView.as_view()),
    # url(r'^artist_create/$', views.ArtistCreateView.as_view()),

    url(r'^tracks_list/$', views.TrackListView.as_view()),
    url(r'^tracks_detail/(?P<slug>.+)/$', views.TrackDetailView.as_view()),
    # url(r'^tracks_create/$', views.TrackCreateView.as_view()),

    # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}),
    # url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}),



    url(r'^login_view/$', 'main.views.login_view', name='login_view'),
    url(r'^logout_view/$', 'main.views.logout_view', name='logout_view'),

    url(r'^signup/$', 'main.views.signup', name='signup_view'),

    url(r'^regiser/$', CreateView.as_view(template_name='register.html',
                                          form_class=CustomUserCreationForm,
                                          success_url='/'))
    ]

