from rest_framework import serializers
from .models import Planet, Terrain, Climate


class TerrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terrain
        fields = ['name']
        read_only_fields = ("id",)


class ClimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climate
        fields = ['name']
        read_only_fields = ("id",)


class PlanetSerializer(serializers.ModelSerializer):
    terrains = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Terrain.objects.all(),

    )
    climates = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Climate.objects.all()
    )

    class Meta:
        model = Planet
        fields = ['name', 'population', 'terrains', 'climates']

    def create(self, validated_data):
        terrains_data = validated_data.pop('terrains')
        climates_data = validated_data.pop('climates')
        planet = Planet.objects.create(**validated_data)

        for terrain_name in terrains_data:
            terrain, _ = Terrain.objects.get_or_create(name=terrain_name)
            planet.terrains.add(terrain)

        for climate_name in climates_data:

            climate, _ = Climate.objects.get_or_create(name=climate_name)
            planet.climates.add(climate)

        return planet

    def update(self, instance, validated_data):
        terrains_data = validated_data.pop('terrains')
        climates_data = validated_data.pop('climates')

        instance.name = validated_data.get('name', instance.name)
        instance.population = validated_data.get('population', instance.population)
        instance.save()

        instance.terrain.clear()
        for terrain_data in terrains_data:
            terrain, _ = Terrain.objects.get_or_create(**terrain_data)
            instance.terrains.add(terrain)

        instance.climates.clear()
        for climate_data in climates_data:
            climate, _ = Climate.objects.get_or_create(**climate_data)
            instance.climates.add(climate)

        return instance
