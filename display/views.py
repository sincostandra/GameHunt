from django.shortcuts import get_object_or_404, render
from display.models import Game
from search.models import Game

# Create your views here.
def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})

def game_detail(request, id):
    game = get_object_or_404(Game, id=id)
    return render(request, 'game_detail.html', {'game': game})
