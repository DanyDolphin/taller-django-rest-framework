'''Playlists' views.'''

# Django
from django.http import HttpResponse

# Django REST Framework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

# Models
from playlists.models import Playlist

# Serializers
from playlists.serializers import PlaylistModelSerializer
from songs.serializers import SongModelSerializer


class PlaylistViewSet(ModelViewSet):
    '''Playlist model viewset'''
    queryset = Playlist.objects.all()
    serializer_class = PlaylistModelSerializer

    @action(detail=True)
    def songs(self, request, pk=None):
        playlist = self.get_object()
        songs =playlist.songs
        return Response(SongModelSerializer(songs, many=True).data)