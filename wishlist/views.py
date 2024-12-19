import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import WishlistForm
from .models import Wishlist
from search.models import Game
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.
@login_required
def view_wishlist(request):
    wishlist_entries = Wishlist.objects.select_related('game').filter(user=request.user)
    if request.user.is_superuser:
        role = 'admin'
    else:
        role = 'user' 
    context = {
        'wishlist_entries': wishlist_entries,
        'role': role
    }
    return render(request, 'wishlist.html', {'wishlist_entries': wishlist_entries})

@login_required
def create_wishlist(request, game_id):
    form = WishlistForm(request.POST or None, initial={'game': game_id})

    if form.is_valid() and request.method == "POST":
        wishlist = form.save(commit=False)
        wishlist.user = request.user
        wishlist.save()
        return redirect('wishlist:view_wishlist')

    context = {
        'form': form,
        'game_id': game_id
    }
    return render(request, "create_wishlist.html", context)

@login_required
@csrf_exempt
def delete_wishlist(request, id):
    wishlist = Wishlist.objects.get(pk = id)
    wishlist.delete()
    return HttpResponseRedirect(reverse('wishlist:view_wishlist'))

@login_required
@csrf_exempt
def show_json(request):
    if not request.user.is_authenticated:
        return JsonResponse({'message': 'User not authenticated', 'status': 401}, status=401)
    data = Wishlist.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@require_POST
@login_required
@csrf_exempt  
def add_wishlist_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            game_wishlisted = Game.objects.get(pk=data['game_id'])

            if Wishlist.objects.filter(game=game_wishlisted, user=request.user).exists():
                return JsonResponse({"status": "info", "message": "Game already in wishlist"}, status=200)

            new_game = Wishlist.objects.create(
                game=game_wishlisted,
                user=request.user  # Ensure the user is set
            )
            new_game.save()
            return JsonResponse({"status": "success"}, status=200)
        except Game.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Game not found"}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    else:
        return JsonResponse({'message': 'BAD REQUEST', 'status': 400}, status=400)

@login_required
def get_wishlist_ajax(request):
    wishlist_entries = Wishlist.objects.select_related('game').filter(user=request.user)
    data = {
        'wishlist': [
            {
                'id': entry.id,
                'game__name': entry.game.name,
                'game__developer': entry.game.developer,
                'game__genre': entry.game.genre,
                'game__harga': entry.game.harga,
                'game__ratings': entry.game.ratings,
                'game__toko1': entry.game.toko1,
                'game__alamat1': entry.game.alamat1,
            }
            for entry in wishlist_entries
        ]
    }
    return JsonResponse(data)

@csrf_exempt
def delete_wishlist_flutter(request, id):
    if request.method == 'DELETE':
        try:
            wishlist = Wishlist.objects.get(pk=id)
            wishlist.delete()
            return JsonResponse({"status": "success"}, status=200)
        except Wishlist.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Wishlist item not found"}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed', 'status': 405}, status=405)