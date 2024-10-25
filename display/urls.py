from django.urls import path
from display.views import game_list, game_detail

app_name = 'display'

urlpatterns = [
    path('', game_list, name='game_list'),  # List of all games
    path('<uuid:id>/', game_detail, name='game_detail')  # Detail for each game
]