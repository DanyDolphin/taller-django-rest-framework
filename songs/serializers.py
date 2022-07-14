'''Songs' serializers.'''

# Django REST Framework
from dataclasses import fields
from rest_framework import serializers

# Models
from songs.models import Song

class SongSerializer(serializers.Serializer):
    '''Song serializer'''

    name = serializers.CharField(
        max_length=100,
        required=True,
        allow_null=False,
        allow_blank=False
    )

    author = serializers.CharField(
        max_length=100
    )

    genre = serializers.ChoiceField(
        choices=Song.GENRE_CHOICES
    )

    def create(self, data):
        song = Song(**data)
        song.save()
        return song

class SongModelSerializer(serializers.ModelSerializer):
    '''Song model serializer'''

    class Meta:
        '''Meta class'''
        model = Song
        fields = '__all__'
        read_only_fields = ('id',)