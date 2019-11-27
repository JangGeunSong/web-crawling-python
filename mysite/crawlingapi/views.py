from .models import MovieInfo
from rest_framework import viewsets
from .serializers import MovieInfoSerializer

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieInfo
    serializer_class = MovieInfoSerializer