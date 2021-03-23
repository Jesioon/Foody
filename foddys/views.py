from django.shortcuts import render

def index(request):
    """Homepage"""
    return render(request, 'foddys/index.html')

def recipes(request):
    """Page with recipes lists"""
    return render(request, 'foddys/recipes.html')

