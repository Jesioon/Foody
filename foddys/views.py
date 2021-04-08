from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from .models import Recipe
from .forms import RecipeForm

def index(request):
    """Homepage"""
    recipes = Recipe.objects.order_by('-publication_date')
    images = []
    for recipe in recipes:
        images.append(recipe.image)
        if len(images) == 3:
            break

    context = {'images': images}
    return render(request, 'foddys/index.html', context)

def recipes(request):
    """Page with recipes lists"""
    return render(request, 'foddys/recipes.html')

def recipe(request):
    """Page with single recipe"""
    return render(request, 'foddys/recipe.html')

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