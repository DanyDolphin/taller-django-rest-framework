'''Songs' admin sites.'''

# Django
from django.contrib import admin

# Models
from songs.models import Song

class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'genre',)

admin.site.register(Song, SongAdmin)
