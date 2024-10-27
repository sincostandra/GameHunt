from django.shortcuts import render,redirect,reverse, get_object_or_404
from search.models import Game
from search.forms import GameForm
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def show_search(request):
     # Periksa apakah pengguna adalah superuser
    if request.user.is_superuser:
        role = 'admin'
    else:
        role = 'user'  # atau bisa diganti sesuai kebutuhan

    context = {
        'role': role 
    }
    return render(request, "search.html", context)

@login_required
def show_json(request):
    data = Game.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required
def show_json_by_id(request, id):
    # Dapatkan objek Game berdasarkan id atau kembalikan 404 jika tidak ditemukan
    game = get_object_or_404(Game, pk=id)
    # Serialisasi objek Game menjadi JSON
    return HttpResponse(serializers.serialize("json", [game]), content_type="application/json")


@login_required
@csrf_exempt
@require_POST
def edit_game_ajax(request, id):
    # Pastikan hanya superuser yang bisa mengakses
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to perform this action.")

    # Mendapatkan game berdasarkan id atau mengembalikan 404 jika tidak ditemukan
    game = Game.objects.get(pk=id)

    # Menggunakan GameForm dengan instance game untuk memvalidasi data POST
    form = GameForm(request.POST or None, instance=game)
    
    if form.is_valid():
        form.save()  # Menyimpan perubahan
        return HttpResponse("Game updated successfully!", status=200)
    else:
        return HttpResponse("Error updating game.", status=400)

@login_required
def delete_game(request, id):
    # Pastikan hanya superuser yang bisa mengakses
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to perform this action.")

    # Get game berdasarkan id
    game = Game.objects.get(pk=id)
    # Hapus game
    game.delete()
    return HttpResponseRedirect(reverse('search:show_search'))

@login_required
@csrf_exempt
@require_POST
def add_game_entry_ajax(request):
    # Pastikan hanya superuser yang bisa mengakses
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to perform this action.")

    # Extract data from the POST request
    name = request.POST.get("name")
    year = request.POST.get("year")
    description = request.POST.get("description")
    developer = request.POST.get("developer")
    genre = request.POST.get("genre")
    ratings = request.POST.get("ratings")
    harga = request.POST.get("harga")
    toko1 = request.POST.get("toko1")
    alamat1 = request.POST.get("alamat1")
    toko2 = request.POST.get("toko2", "")  # Optional
    alamat2 = request.POST.get("alamat2", "")  # Optional
    toko3 = request.POST.get("toko3", "")  # Optional
    alamat3 = request.POST.get("alamat3", "")  # Optional

    # Create and save the new Game entry
    new_game = Game(
        name=name,
        year=int(year) if year else None,
        description=description,
        developer=developer,
        genre=genre,
        ratings=float(ratings) if ratings else 0.0,
        harga=int(harga) if harga else 0,
        toko1=toko1,
        alamat1=alamat1,
        toko2=toko2,
        alamat2=alamat2,
        toko3=toko3,
        alamat3=alamat3,
    )
    new_game.save()

    return HttpResponse(b"CREATED", status=201)