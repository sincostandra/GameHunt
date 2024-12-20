from django.urls import path
from display.views import game_list, game_detail, add_comment_ajax, show_json_by_id, json_allcomments, delete_comment, create_comment_flutter, delete_comment_flutter

app_name = 'display'

urlpatterns = [
    path('list', game_list, name='game_list'),  # List of all games
    path('<uuid:id>/', game_detail, name='game_detail'),  # Detail for each game
    path('add-comment-ajax/<uuid:id>/', add_comment_ajax, name='add_comment_ajax'),  # Add comment via AJAX
    path('show-json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),  # Show JSON data
    path('show-json-allcomments', json_allcomments, name='show_json_allcomments'),  # Show JSON data for all comments
    path('delete-comment/<str:id>/', delete_comment, name='delete_comment'),  # Delete a comment
    path('create-comment-flutter/', create_comment_flutter, name='create_comment_flutter'),  # Create a comment via Flutter
    path('delete-comment-flutter/<str:id>/', delete_comment_flutter, name='delete_comment_flutter'),  # Delete a comment via Flutter
]