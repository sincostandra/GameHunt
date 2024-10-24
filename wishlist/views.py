from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game, Wishlist


def show_wishlist(request):
    context = {
        'app_name': 'GameHunt',
        'app_description': 'Temukan game PS4 favoritmu dengan mudah di Jakarta, lengkap dengan ulasan, promosi, dan pencarian berdasarkan lokasi untuk pengalaman belanja yang praktis dan menyenangkan!'
    }

    return render(request, 'wishlist.html', context)

@login_required
def game_list(request):
    games = Game.objects.all()
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'game_list.html', {'games': games, 'wishlist': wishlist})

@login_required
def add_to_wishlist(request, game_id):
    game = Game.objects.get(id=game_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.games.add(game)
    return redirect('game_list')

@login_required
def remove_from_wishlist(request, game_id):
    game = Game.objects.get(id=game_id)
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist.games.remove(game)
    return redirect('wishlist')
