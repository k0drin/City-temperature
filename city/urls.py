from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, get_stats

router = DefaultRouter()
router.register(r'city', CityViewSet, basename='city')

urlpatterns = [
    path('', include(router.urls)),
    path('stats/', get_stats),
]

