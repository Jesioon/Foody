from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Recipe, Meal, WorldCuisine
from .forms import RecipeForm

def index(request):
    """Homepage"""
    recipes = Recipe.objects.order_by('-publication_date')
    meals = Meal.objects.all()
    countries = WorldCuisine.objects.all()

    recipes_recent, recipes_quick, meals_context, countries_context = [], [], {}, {}

    recipes_recent = recipes[:3]
    recipes_quick = recipes.order_by('time_need')[:3]

    
    for meal in meals:
        meals_context[meal.mealTime] = meal.recipe_set.order_by('-publication_date')[:3]

    for country in countries:
        countries_context[country.country] = country.recipe_set.order_by('-publication_date')[:3]

    context = {'recipes_recent': recipes_recent, 'recipes_quick': recipes_quick, 'meals_context': meals_context, 'countries_context': countries_context}

    print(meals_context)
    return render(request, 'foddys/index.html', context)

def recipes(request, typeOf, recipeType):
    if typeOf == 'country':
        chosenItem = WorldCuisine.objects.get(country=recipeType)

    elif typeOf == 'mealTime':
        chosenItem = Meal.objects.get(mealTime=recipeType)

    elif typeOf == 'moje' and recipeType == 'Moje':
        recipes = Recipe.objects.filter(owner=request.user).order_by('-publication_date')
        context = {'recipes': recipes, 'typeOf': typeOf, 'recipeType': recipeType}
        return render(request, 'foddys/recipes.html', context)
    
    recipes = chosenItem.recipe_set.order_by('-likes')    
    context ={'recipes': recipes, 'typeOf': typeOf, 'recipeType': recipeType}

    return render(request, 'foddys/recipes.html', context)

def recipe(request, recipe_id):
    """Page with single recipe"""
    recipe = Recipe.objects.get(id=recipe_id)

    if recipe.level == 'ES':
        recipeLevel = 'Łatwe'
    elif recipe.level == 'MM':
        recipeLevel = 'Średnie'
    elif recipe.level == 'HR':
        recipeLevel = 'Trudne'
        
    context = {'recipe': recipe, 'recipeLevel': recipeLevel}
    return render(request, 'foddys/recipe.html', context)

@login_required
def new_recipe(request):
    """Add new recipe as user"""
    if request.method != 'POST':
        form = RecipeForm()
    else:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.owner = request.user
            new_recipe.save()
            return redirect('foddys:index')

    context = {'form': form}
    return render(request, 'foddys/new_recipe.html', context)