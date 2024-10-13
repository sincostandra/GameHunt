from django.urls import path
from search.views import show_search, create_game_entry,show_json

app_name = 'search'

urlpatterns = [
    path('', show_search, name='show_search'),
    path('create-game-entry', create_game_entry, name='create_game_entry'),
    path('json/', show_json, name='show_json'),

]