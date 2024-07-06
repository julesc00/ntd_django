from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=255, unique=True)
    population = models.BigIntegerField()
    terrain = models.ManyToManyField("Terrain")
    climates = models.ManyToManyField("Climate")

    def __str__(self):
        return self.name


TERRAIN_CHOICES = (
    ("desert", "Desert"),
    ("grasslands", "Grasslands"),
    ("mountains", "Mountains"),
    ("swamp", "Swamp"),
    ("forests", "Forests"),
    ("jungle", "Jungle"),
    ("tundra", "Tundra"),
    ("ocean", "Ocean"),
    ("islands", "Islands"),
    ("cities", "Cities"),
    ("caves", "Caves"),
    ("unknown", "Unknown"),
)


class Terrain(models.Model):
    name = models.CharField(max_length=255, choices=TERRAIN_CHOICES, default="unknown")

    def __str__(self):
        return self.name


class Climate(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
