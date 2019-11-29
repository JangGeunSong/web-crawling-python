from .models import MovieInfo
from rest_framework import viewsets
from rest_framework import filters # search를 위해 임포트
from .serializers import MovieInfoSerializer

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet): # Django rest_framework 에 내장된 Viewsets을 활용
    queryset = MovieInfo.objects.all()
    serializer_class = MovieInfoSerializer
    # date값을 클라이언트 사이드에서 입력받으면 이를 읽어들여와 해당하는 필드의 값만 보내주고 나머지는 보내지 않는 작업을 추가
    filter_backends = [filters.SearchFilter]
    search_fields = ["date"]