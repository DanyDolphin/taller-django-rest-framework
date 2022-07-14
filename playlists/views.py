'''Playlists' views.'''

# Django
from django.http import HttpResponse

def index(request):
    '''Playlists' index view'''
    return HttpResponse("Hello, world. You're at the playlists index.")
