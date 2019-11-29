from django.db import models

# Create your models here.
class MovieInfo(models.Model): # 영화 정보를 저장할 DB 테이블 설계
    ID = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    Link = models.CharField(max_length=256)
    date = models.CharField(max_length=9)
    # ID title Link date 4개의 열로 구성된 영화정보
    
    def __str__(self):
        return self.title
