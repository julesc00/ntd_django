from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from api.models import Planet, Terrain, Climate
from api.serializers import PlanetSerializer, TerrainSerializer, ClimateSerializer
from api.queries import planets_query
from api.helpers import APIClient


URL = "https://swapi-graphql.netlify.app/.netlify/functions/index"

QUERY = planets_query()


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

    client = APIClient(url=URL, query=QUERY)
    data = client.get()

    @action(detail=False, methods=['get'])
    def fetch_and_create_planets(self, request):
        created_planets = []
        for planet_data in self.data['data']['allPlanets']['planets']:
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
