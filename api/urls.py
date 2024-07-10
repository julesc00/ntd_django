from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PlanetViewSet, TerrainViewSet, ClimateViewSet

router = DefaultRouter()
router.register(r'api/planets', PlanetViewSet)
router.register(r'terrains', TerrainViewSet)
router.register(r'climates', ClimateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


