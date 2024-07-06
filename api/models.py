from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=255, unique=True)
    population = models.BigIntegerField()
    terrain = models.ManyToManyField("Terrain")
    climates = models.ManyToManyField("Climate")

    def __str__(self):
        return self.name


class Terrain(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Climate(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
