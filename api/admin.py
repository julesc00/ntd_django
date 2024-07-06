from django.contrib import admin

from api.models import Planet, Terrain, Climate

admin.site.register(Planet)
admin.site.register(Terrain)
admin.site.register(Climate)
