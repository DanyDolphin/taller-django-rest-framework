'''Songs' views.'''

# Django
from django.http import HttpResponse

# Django REST Framework
from rest_framework.views import APIView, status
from rest_framework.response import Response

# Models
from songs.models import Song

class ListCreateSongs(APIView):
    '''View to list and create songs'''

    def get(self, request):
        '''Returns a list of all songs'''
        queryset = Song.objects.all()
        return Response(
            [{
                'name': song.name,
                'author': song.author,
                'genre': song.genre
            } for song in queryset]
        )

    def post(self, request):
        '''Creates a song'''
        song = Song(
            name=request.data['name'],
            author=request.data['author'],
            genre=request.data['genre']
        )
        song.save()
        return Response(
            {
                'name': song.name,
                'author': song.author,
                'genre': song.genre
            },
            status.HTTP_201_CREATED
        )
