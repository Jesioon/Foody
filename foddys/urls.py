"""Define patterns URL addresses for foddy"""

from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'foddys'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Pages with single type of recipes
    path('recipes/<str:typeOf>/<str:recipeType>/', views.recipes, name='recipes'),
    # Page with single recipe
    path('recipe/', views.recipe, name='recipe'),
    # Add new recipe as user
    path('new_recipe/', views.new_recipe, name='new_recipe'),
]
