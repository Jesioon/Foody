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

    return render(request, 'foddys/index.html', context)

def recipes(request, typeOf, recipeType):
    if typeOf == 'country':
        chosenItem = WorldCuisine.objects.get(country=recipeType)

    elif typeOf == 'mealTime':
        chosenItem = Meal.objects.get(mealTime=recipeType)

    elif typeOf == 'search' and recipeType == 'Search':
        search_value = request.POST['name'].lower()
        recipes = Recipe.objects.all()
        chosenItem = []
        for recipe in recipes: 
            if recipe.recipe_name.lower().count(search_value) > 0:
                chosenItem.append(recipe)
          
        context = {'recipes': chosenItem, 'typeOf': typeOf, 'recipeType': recipeType}
        return render(request, 'foddys/recipes.html', context)

    try:
        recipes = chosenItem.recipe_set.order_by('-likes')    
    except UnboundLocalError:
        return redirect('foddys:index')
        print('Nie ma chosenItem')

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
        
    recipeOwner = False

    if recipe.owner == request.user:
        recipeOwner = True

    context = {'recipe': recipe, 'recipeLevel': recipeLevel, 'recipeOwner': recipeOwner}
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

@login_required
def my_recipes(request):
    recipes = Recipe.objects.filter(owner=request.user).order_by('-publication_date')
    context = {'recipes': recipes}
    return render(request, 'foddys/my_recipes.html', context)

@login_required
def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if recipe.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = RecipeForm(instance=recipe)
    else:
        form = RecipeForm(instance=recipe, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('foddys:my_recipes')

    context = {'recipe': recipe, 'form': form}
    return render(request, 'foddys/edit_recipe.html', context)