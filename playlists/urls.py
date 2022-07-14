'''Playlists' URLs'''

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter

# Views
from .views import *


router = SimpleRouter()
router.register('', PlaylistViewSet, basename='playlists')


urlpatterns = [
    path('', include(router.urls))
]

urlpatterns = format_suffix_patterns(urlpatterns)