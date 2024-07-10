from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, default=None)
    population = models.BigIntegerField(default=None, blank=True, null=True)
    terrain = models.ManyToManyField("Terrain", blank=True, related_name="planets")
    climates = models.ManyToManyField("Climate", blank=True, related_name="planets")

    def __str__(self):
        return self.name


class Terrain(models.Model):
    name = models.CharField(max_length=255, blank=True, default=None)

    def __str__(self):
        return self.name


class Climate(models.Model):
    name = models.CharField(max_length=255, blank=True, default=None)

    def __str__(self):
        return self.name
