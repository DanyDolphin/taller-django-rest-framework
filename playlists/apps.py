'''Playlists' app config'''

# Django
from django.apps import AppConfig


class PlaylistsConfig(AppConfig):
    '''Playlists' app config'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playlists'
    verbose_name = 'Playlists'