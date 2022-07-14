'''Users' views.'''

# Django
from django.http import HttpResponse

def index(request):
    '''Users' index view'''
    return HttpResponse("Hello, world. You're at the users index.")
