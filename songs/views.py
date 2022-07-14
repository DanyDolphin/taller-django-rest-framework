'''Songs' views.'''

# Django
from django.http import HttpResponse

# Django REST Framework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, status
from rest_framework.response import Response

# Models
from songs.models import Song

# Serializers
from songs.serializers import SongSerializer, SongModelSerializer

class ListCreateSongs(ListCreateAPIView):
    '''View to list and create songs'''

    queryset = Song.objects.all()
    serializer_class = SongModelSerializer

class RetrieveUpdateDestroySongs(RetrieveUpdateDestroyAPIView):
    '''View to retrieve, update or destroy a song'''

    queryset = Song.objects.all()
    serializer_class = SongModelSerializer
