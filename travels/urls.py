from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TravelViewSet

router = DefaultRouter()
router.register('', TravelViewSet)
urlpatterns = [
    path('', include(router.urls)),
]