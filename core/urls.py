
from django.contrib import admin
from django.urls import path, include

from api.views import PlanetViewSet, TerrainViewSet, ClimateViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("api.urls")),
]