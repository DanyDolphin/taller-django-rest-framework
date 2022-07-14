'''Playlists' models'''

# Utilities
from uuid import uuid4

# Django
from django.db import models

class Playlist(models.Model):
    '''Playlist model.'''

    id = models.UUIDField(default=uuid4, primary_key=True)

    name = models.CharField(
        max_length=100,
        help_text='The name of the playlist'
    )
    
    is_private = models.BooleanField(
        default=True,
        help_text='Whether to let other users to watch/edit the playlist'
    )

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        help_text='The owner of the playlist'
    )

    songs = models.ManyToManyField(
        'songs.Song',
        help_text='the assosiated songs'
    )
