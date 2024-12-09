from django.shortcuts import render,redirect,reverse, get_object_or_404
from search.models import Game
from search.forms import GameForm
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
import json
from django.http import JsonResponse

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


@csrf_exempt
def create_game_flutter(request):
    if request.method == 'POST':
        try:
            # Parse JSON body from request
            data = json.loads(request.body)

            # Buat instance Game baru
            new_game = Game.objects.create(
                name=data["name"],
                year=int(data.get("year", 0)) if data.get("year") else None,
                description=data["description"],
                developer=data["developer"],
                genre=data["genre"],
                ratings=float(data["ratings"]),
                harga=int(data["harga"]),
                toko1=data["toko1"],
                alamat1=data["alamat1"],
                toko2=data.get("toko2", ""),  # Optional
                alamat2=data.get("alamat2", ""),  # Optional
                toko3=data.get("toko3", ""),  # Optional
                alamat3=data.get("alamat3", ""),  # Optional
            )

            # Simpan instance Game
            new_game.save()

            return JsonResponse({"status": "success", "id": str(new_game.id)}, status=200)
        except KeyError as e:
            return JsonResponse({"status": "error", "message": f"Missing field: {str(e)}"}, status=400)
        except ValueError as e:
            return JsonResponse({"status": "error", "message": f"Invalid value: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
    

@csrf_exempt
def edit_game_flutter(request, game_id):
    # game_id adalah UUID dalam bentuk string
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            # game_uuid = UUID(game_id)
            game = Game.objects.get(id=game_id)

            if "name" in data: game.name = data["name"]
            if "year" in data:
                game.year = int(data["year"]) if data["year"] else None
            if "description" in data: game.description = data["description"]
            if "developer" in data: game.developer = data["developer"]
            if "genre" in data: game.genre = data["genre"]
            if "ratings" in data: game.ratings = float(data["ratings"])
            if "harga" in data: game.harga = int(data["harga"])
            if "toko1" in data: game.toko1 = data["toko1"]
            if "alamat1" in data: game.alamat1 = data["alamat1"]
            if "toko2" in data: game.toko2 = data["toko2"]
            if "alamat2" in data: game.alamat2 = data["alamat2"]
            if "toko3" in data: game.toko3 = data["toko3"]
            if "alamat3" in data: game.alamat3 = data["alamat3"]

            game.save()

            return JsonResponse({"status": "success"}, status=200)
        except Game.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Game not found"}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)


@csrf_exempt
def delete_game_flutter(request, game_id):
    if request.method == 'DELETE':
        try:
            # game_uuid = UUID(game_id)
            game = Game.objects.get(pk=game_id)
            game.delete()
            return JsonResponse({"status": "success"}, status=200)
        except Game.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Game not found"}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)


def game_list_json(request):
    games = Game.objects.all()
    data = []
    for g in games:
        data.append({
            'id': str(g.id),
            'fields': {
                'name': g.name,
                'year': g.year,
                'description': g.description,
                'developer': g.developer,
                'genre': g.genre,
                'ratings': g.ratings,
                'harga': g.harga,
                'toko1': g.toko1,
                'alamat1': g.alamat1,
                'toko2': g.toko2,
                'alamat2': g.alamat2,
                'toko3': g.toko3,
                'alamat3': g.alamat3,
            }
        })
    return JsonResponse(data, safe=False)


@login_required
def get_user_role(request):
    role = "admin" if request.user.is_superuser else "user"
    return JsonResponse({"role": role})