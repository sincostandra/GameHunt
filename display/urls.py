from django.urls import path
from display.views import game_list, game_detail, add_comment_ajax, show_json_by_id

app_name = 'display'

urlpatterns = [
    path('list', game_list, name='game_list'),  # List of all games
    path('<uuid:id>/', game_detail, name='game_detail'),  # Detail for each game
    path('add-comment-ajax', add_comment_ajax, name='add_comment_ajax'),  # Add comment via AJAX
    path('show-json/<uuid:id>', show_json_by_id, name='show_json_by_id'),  # Show JSON data
]