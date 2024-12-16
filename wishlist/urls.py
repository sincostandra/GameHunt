from django.urls import path
from wishlist.views import view_wishlist, delete_wishlist, create_wishlist, show_json, add_wishlist_ajax, get_wishlist_ajax, delete_wishlist_flutter

app_name = 'wishlist'

urlpatterns = [
    path('', view_wishlist, name='view_wishlist'),
    path('delete-wishlist/<uuid:id>/', delete_wishlist, name='delete_wishlist'),
    path('json/', show_json, name='show_json'),
    path('create-wishlist/<uuid:game_id>/', create_wishlist, name='create_wishlist'),
    path('add-wishlist-ajax/', add_wishlist_ajax, name='add_wishlist_ajax'),
    path('get-wishlist/', get_wishlist_ajax, name='get_wishlist'),
    path('delete-wishlist-flutter/<uuid:id>/', delete_wishlist_flutter, name='delete_wishlist_flutter')
]