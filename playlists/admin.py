'''Playlists' admin sites.'''

# Django
from django.contrib import admin

# Models
from playlists.models import Playlist

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_private')

admin.site.register(Playlist, PlaylistAdmin)
