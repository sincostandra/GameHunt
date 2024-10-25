from django.urls import path
from search.views import show_search, create_game_entry,show_json,edit_game,delete_game,add_game_entry_ajax

app_name = 'search'

urlpatterns = [
    path('', show_search, name='show_search'),
    path('create-game-entry', create_game_entry, name='create_game_entry'),
    path('json/', show_json, name='show_json'),
    path('edit-game/<uuid:id>', edit_game, name='edit_game'),
    path('delete/<uuid:id>', delete_game, name='delete_game'),
    path('create-game-entry-ajax', add_game_entry_ajax, name='add_game_entry_ajax'),
]