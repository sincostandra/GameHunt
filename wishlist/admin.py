from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import Game, Wishlist

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'developer', 'genre', 'rating', 'price', 'store')
    search_fields = ('name', 'developer', 'genre')

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'game')
    search_fields = ('user__username', 'game__name')

