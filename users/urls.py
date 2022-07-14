'''Users' URLs'''

# Django
from django.urls import path

# Views
from .views import *

urlpatterns = [
    path('', index, name='index'),
]
