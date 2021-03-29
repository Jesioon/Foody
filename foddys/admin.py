from django.contrib import admin

from .models import Recipe, Meal, WorldCuisine

admin.site.register(Recipe)
admin.site.register(Meal)
admin.site.register(WorldCuisine)

