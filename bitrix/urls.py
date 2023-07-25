from rest_framework.routers import DefaultRouter
from bitrix.views import *
from django.urls import path


router = DefaultRouter()
router.register(r'tagat', TagatViewSet)
router.register(r'tdata', TdataViewSet)
router.register(r'temail', TemailViewSet)
router.register(r'tklient', TklientViewSet)
router.register(r'ttarif', TtarifViewSet)
router.register(r'twialon100', Twialon100ViewSet)


urlpatterns = router.urls


