from django.shortcuts import render, redirect, get_object_or_404
from .forms import WishlistForm
from .models import Wishlist
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Create your views here.
def add_to_wishlist(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, game=game)
    if created:
        messages.success(request, f"'{game.name}' has been added to your wishlist!")
    else:
        messages.info(request, f"'{game.name}' is already in your wishlist.")
    return redirect('view_wishlist')

def view_wishlist(request):
    wishlists = Wishlist.objects.all()
    # wishlists = Wishlist.objects.filter(user=request.user)
    context = {
        'wishlists': wishlists,
    }
    return render(request, 'wishlist.html', context)

def delete_wishlist(request, id):
    wishlist = Wishlist.objects.get(pk = id)
    wishlist.delete()
    return HttpResponseRedirect(reverse('wishlist:wishlist'))

def show_json(request):
    data = Wishlist.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = Wishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Wishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Wishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")