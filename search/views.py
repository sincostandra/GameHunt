from django.shortcuts import render,redirect
from search.models import Game
from search.forms import GameForm

def show_search(request):
    game_entries = Game.objects.all()
    context = {
        'name': 'Dummy',
        'last_login' : "Dummy",
        'game_entries' :game_entries
    }

    return render(request, "search.html", context)


def create_game_entry(request):
    form = GameForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('search:show_search')  # Adjust the redirect based on your URL configuration

    context = {'form': form}
    return render(request, "create_game_entry.html", context)
