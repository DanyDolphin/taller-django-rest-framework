'''Playlists' admin sites.'''

# Django
from django.contrib import admin

# Models
from playlists.models import Playlist

admin.site.register(Playlist)
