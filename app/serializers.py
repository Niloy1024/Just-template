from rest_framework import serializers
from .models import Album,Track

class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']

# For each album object, tracks should be fetched from database

class TrackSerializer(serializers.ModelSerializer):
    # album = serializers.CharField(source='album.album_name')
    class Meta:
        model = Track
        fields  = '__all__'