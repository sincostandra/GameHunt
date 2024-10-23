from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game, Wishlist

@login_required
def add_to_wishlist(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, game=game)
    if created:
        message = f"{game.name} has been added to your wishlist!"
    else:
        message = f"{game.name} is already in your wishlist."
    return redirect('wishlist')

@login_required
def remove_from_wishlist(request, game_id):
    wishlist_item = get_object_or_404(Wishlist, user=request.user, game__id=game_id)
    wishlist_item.delete()
    return redirect('wishlist')

@login_required
def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

