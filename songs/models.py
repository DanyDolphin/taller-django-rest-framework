'''Songs' models.'''

# Utilities
from uuid import uuid4

# Django
from django.db import models

# Create your models here.
class Song(models.Model):
    '''Song model.'''

    id = models.UUIDField(default=uuid4, primary_key=True)

    name = models.CharField(
        max_length=100,
        help_text='The name of the song'
    )

    GENRE_CHOICES = (
        ('reggaeton', 'Reggaeton'),
        ('bachata', 'Bachata'),
        ('rock', 'Rock'),
        ('indie', 'Indie'),
        ('banda', 'Banda'),
        ('hiphop', 'Hip hop'),
        ('balada', 'Balada'),
    )
    genre = models.CharField(
        choices=GENRE_CHOICES,
        max_length=50,
        help_text='The genre of the song'
    )

    author = models.CharField(
        max_length=100,
        help_text='The author and featurings of the song'
    )

    lyrics = models.TextField(
        null=True,
        blank=True,
        help_text='The original lyrics of the song'
    )
