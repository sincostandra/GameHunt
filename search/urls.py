from django.urls import path
from search.views import show_search,show_json,delete_game,add_game_entry_ajax,show_json_by_id, edit_game_ajax

app_name = 'search'

urlpatterns = [
    path('', show_search, name='show_search'),
    path('json/', show_json, name='show_json'),
    path('delete/<uuid:id>', delete_game, name='delete_game'),
    path('create-game-entry-ajax', add_game_entry_ajax, name='add_game_entry_ajax'),
    path('json/<uuid:id>', show_json_by_id, name='show_json'),
    path('edit-game-ajax/<uuid:id>', edit_game_ajax, name = 'edit_game_ajax')


]