'''Songs' views.'''

# Django
from django.http import HttpResponse

# Django REST Framework
from rest_framework.views import APIView, status
from rest_framework.response import Response

# Models
from songs.models import Song

# Serializers
from songs.serializers import SongSerializer, SongModelSerializer

class ListCreateSongs(APIView):
    '''View to list and create songs'''

    def get(self, request):
        '''Returns a list of all songs'''
        queryset = Song.objects.all()
        return Response(
            SongModelSerializer(queryset, many=True).data
        )

    def post(self, request):
        '''Creates a song'''
        serializer = SongModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        song = serializer.save()
        return Response(
            SongModelSerializer(song).data,
            status.HTTP_201_CREATED
        )
