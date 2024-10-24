# urls.py
from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.show_wishlist, name='show_wishlist'),
    path('', views.game_list, name='game_list'),
    path('add-to-wishlist/<int:game_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:game_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
