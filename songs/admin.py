'''Songs' admin sites.'''

# Django
from django.contrib import admin

# Models
from songs.models import Song

admin.site.register(Song)
