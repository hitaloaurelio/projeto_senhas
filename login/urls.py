from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logar', views.Logar, name='logar'),
    path('home', views.home, name='home'),
]