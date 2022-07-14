'''Songs' URLs'''

# Django
from django.urls import path

# Django REST Framework
from rest_framework.urlpatterns import format_suffix_patterns

# Views
from .views import *

urlpatterns = [
    path('', ListCreateSongs.as_view(), name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)