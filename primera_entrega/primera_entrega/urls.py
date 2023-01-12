from django.contrib import admin
from django.urls import path

from .views import hola_mundo

from players.views import create_player, create_club, create_tecnico, list_clubs, list_players, list_tecnicos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', hola_mundo),
    path('create-player/', create_player),
    path('create-club/', create_club),
    path('create-tecnico/', create_tecnico),
    path('list-players/', list_players),
    path('list-clubs/', list_clubs),
    path('list-tecnicos/', list_tecnicos),
]
