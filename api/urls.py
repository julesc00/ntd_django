from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PlanetViewSet

router = DefaultRouter()
router.register(r'planets', PlanetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


