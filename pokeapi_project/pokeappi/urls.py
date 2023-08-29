from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_pokemon, name='search_pokemon'),
    path('ability/<str:ability_name>/', views.ability_detail, name='ability_detail'),
]
