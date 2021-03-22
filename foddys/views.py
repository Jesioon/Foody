from django.shortcuts import render

def index(request):
    """Homepage"""
    return render(request, 'foddys/index.html')