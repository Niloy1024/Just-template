from rest_framework.generics import ListCreateAPIView
from .models import Track,Album
from .serializers import TrackSerializer,AlbumSerializer

class MyModelListCreateView(ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class MyModel2ListCreateView(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


