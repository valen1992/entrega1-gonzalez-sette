from django.shortcuts import render
from django.http import HttpResponse

from .models import Players, Clubs, Tecnicos


# Create your views here.

def create_player(request):
    return HttpResponse("nuevo")

def list_players(request):
    all_players = Players.objects.all
    context= {
        'players': all_players
    }
    return render('list_players', context={})

def create_club(request):
    return HttpResponse("nuevo")

def list_clubs(request):
    all_clubs= Clubs.objects.all
    context= {
        'clubs': all_clubs
    }
    return render('list_clubs', context={})


def create_tecnico(request):
    return HttpResponse("nuevo")

def list_tecnicos(request):
    all_tecnicos = Tecnicos.objects.all
    context= {
        'tecnicos': all_tecnicos
    }
    return render('list_tecnicos', context={})