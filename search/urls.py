<<<<<<< HEAD
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


=======
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


>>>>>>> 320f02c7688d29fe78f1f4130ecbf852bcb527d3
]