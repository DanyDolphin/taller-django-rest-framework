'''Playlists' serializers.'''

# Django REST Framework
from dataclasses import fields
from rest_framework import serializers

# Models
from playlists.models import Playlist


class PlaylistModelSerializer(serializers.ModelSerializer):
    '''Playlist model serializer'''

    class Meta:
        '''Meta class'''
        model = Playlist
        fields = '__all__'
        read_only_fields = ('id',)
