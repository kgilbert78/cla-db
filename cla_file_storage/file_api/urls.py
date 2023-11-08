from rest_framework.routers import DefaultRouter
from .views import FileViewSet, KeywordViewSet

router = DefaultRouter()
router.register(r'files', FileViewSet, basename='files')
router.register(r'keywords', KeywordViewSet, basename='keywords')

urlpatterns = router.urls