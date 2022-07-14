'''Songs' views.'''

# Django
from django.http import HttpResponse

def index(request):
    '''Songs' index view'''
    return HttpResponse("Hello, world. You're at the songs index.")
