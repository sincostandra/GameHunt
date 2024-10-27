import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import WishlistForm
from .models import Wishlist, Game 
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.
def add_to_wishlist(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, game=game)
    if created:
        messages.success(request, f"'{game.name}' has been added to your wishlist!")
    else:
        messages.info(request, f"'{game.name}' is already in your wishlist.")
    return redirect('view_wishlist')

@login_required
def view_wishlist(request):
    wishlist_entries = Wishlist.objects.select_related('game').all()
    role = 'admin' if request.user.is_superuser else 'user'
    context = {
        'wishlist_entries': wishlist_entries,
        'role': role
    }
    return render(request, 'wishlist.html', {'wishlist_entries': wishlist_entries})

@login_required
def create_wishlist(request):
    form = WishlistForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('wishlist:view_wishlist') 

    context = {'form': form}
    return render(request, "create_wishlist.html", context)

@login_required
def delete_wishlist(request, id):
    wishlist = Wishlist.objects.get(pk = id)
    wishlist.delete()
    return HttpResponseRedirect(reverse('wishlist:view_wishlist'))

@login_required
def show_json(request):
    data = Wishlist.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
@require_POST
@login_required
def add_wishlist_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        game_wishlisted = Game.objects.get(pk=data['game_id'])

        new_game = Wishlist.objects.create(
            game = game_wishlisted,
        )

        new_game.save()
        
        return JsonResponse({"status": "success"}, status=200)

    else:
        return JsonResponse({'message': 'BAD REQUEST', 'status': 400}, status=400)

@login_required
def get_wishlist_ajax(request):
    wishlist_entries = Wishlist.objects.select_related('game').all()
    data = {
        'wishlist': [
            {
                'id': entry.id,
                'game__name': entry.game.name,
                'game__developer': entry.game.developer,
                'game__genre': entry.game.genre,
                'game__harga': entry.game.harga,
                'game__ratings': entry.game.ratings,
            }
            for entry in wishlist_entries
        ]
    }
    return JsonResponse(data)