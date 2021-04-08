from django.urls import path, include

from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'users'
urlpatterns = [
    # path('', include('django.contrib.auth.urls')),

    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
]