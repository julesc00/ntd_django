from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import action

from api.models import Planet, Terrain, Climate
from api.serializers import PlanetSerializer, TerrainSerializer, ClimateSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    parser_classes = [JSONParser]

    @method_decorator(csrf_exempt)
    @action(detail=False, methods=['post'])
    def batch_create(self, request):
        created_planets = []

        for planet_data in request.data:
            breakpoint()
            serializer = self.get_serializer(data=planet_data)

            serializer.is_valid(raise_exception=True)
            planet = serializer.save()
            created_planets.append(planet)

        return Response({
            "status": "success",
            "created_planets": [self.get_serializer(planet).data for planet in created_planets]
        }, status=status.HTTP_201_CREATED)


class TerrainViewSet(viewsets.ModelViewSet):
    queryset = Terrain.objects.all()
    serializer_class = TerrainSerializer


class ClimateViewSet(viewsets.ModelViewSet):
    queryset = Climate.objects.all()
    serializer_class = ClimateSerializer
