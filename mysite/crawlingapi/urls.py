from rest_framework import routers
from .views import MovieViewSet

router = routers.DefaultRouter()
router.register('', MovieViewSet, 'movie')

urlpatterns = router.urls