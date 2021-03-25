"""Define patterns URL addresses for foddy"""

from django.urls import path

from . import views

app_name = 'foddys'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Page with recipes lists
    path('recipes/', views.recipes, name='recipes'),
    # Page with single recipe
    path('recipe/', views.recipe, name='recipe'),
    # Add new recipe as user
    path('new_recipe/', views.new_recipe, name='new_recipe'),
]
