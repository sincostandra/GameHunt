from django.forms import ModelForm
from search.models import Game

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = [
            "name", "year", "description", "developer", 
            "genre", "ratings", "harga", 
            "toko1", "alamat1", "toko2", "alamat2", 
            "toko3", "alamat3"
        ]
