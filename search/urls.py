from django.urls import path
from search.views import show_search,show_json,delete_game,add_game_entry_ajax,show_json_by_id, edit_game_ajax,create_game_flutter, edit_game_flutter, delete_game_flutter, game_list_json,get_user_role

app_name = 'search'

urlpatterns = [
    path('', show_search, name='show_search'),
    path('json/', show_json, name='show_json'),
    path('delete/<uuid:id>', delete_game, name='delete_game'),
    path('create-game-entry-ajax', add_game_entry_ajax, name='add_game_entry_ajax'),
    path('json/<uuid:id>', show_json_by_id, name='show_json'),
    path('edit-game-ajax/<uuid:id>', edit_game_ajax, name = 'edit_game_ajax'),
    path('create-game-flutter/', create_game_flutter, name='create_mood_flutter'),
    path('edit-game-flutter/<uuid:game_id>/', edit_game_flutter, name='edit_game_flutter'),
    path('delete-game-flutter/<uuid:game_id>/', delete_game_flutter, name='delete_game_flutter'),
    path('search/json/', game_list_json, name='game_list_json'),
    path('user-role/', get_user_role, name='get_user_role'),
]