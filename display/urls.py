from django.urls import path
from .views import game_list, game_detail

urlpatterns = [
    path('', game_list, name='game_list'),  # List of all games
    path('<uuid:game_id>/', game_detail, name='game_detail'),  # Detail for each game
]