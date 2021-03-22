"""Define patterns URL addresses for foddy"""

from django.urls import path

from . import views

app_name = 'foddys'
urlpatterns = [
    #Homepage
    path('', views.index, name='index'),
]