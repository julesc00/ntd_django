from rest_framework import serializers

from api.models import Terrain, Climate, Planet


class TerrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terrain
        fields = ['id', 'name']


class ClimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climate
        fields = ['id', 'name']


class PlanetSerializer(serializers.ModelSerializer):
    terrains = TerrainSerializer(many=True)
    climates = ClimateSerializer(many=True)

    class Meta:
        model = Planet
        fields = ['id', 'name', 'population', 'terrains', 'climates']

    def create(self, validated_data):

        print(validated_data)

        terrains_data = validated_data.pop('terrains')
        climates_data = validated_data.pop('climates')
        planet = Planet.objects.create(**validated_data)

        for terrain_data in terrains_data:

            terrain, _ = Terrain.objects.get_or_create(**terrain_data)
            planet.terrains.add(terrain)

        for climate_data in climates_data:
            climate, _ = Climate.objects.get_or_create(**climate_data)
            planet.climates.add(climate)

        return planet

    def update(self, instance, validated_data):
        terrains_data = validated_data.pop('terrains')
        climates_data = validated_data.pop('climates')

        instance.name = validated_data.get('name', instance.name)
        instance.population = validated_data.get('population', instance.population)
        instance.save()

        instance.terrains.clear()
        for terrain_data in terrains_data:
            terrain, _ = Terrain.objects.get_or_create(**terrain_data)
            instance.terrains.add(terrain)

        instance.climates.clear()
        for climate_data in climates_data:
            climate, _ = Climate.objects.get_or_create(**climate_data)
            instance.climates.add(climate)

        return instance
