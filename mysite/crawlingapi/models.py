from django.db import models

# Create your models here.
class newsFeed(models.Model):
    newsid = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    articleLink = models.CharField(max_length=256)

    def __str__(self):
        return self.title
