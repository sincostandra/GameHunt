from django import forms
from search.models import Game



class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            "name", "year", "description", "developer", 
            "genre", "ratings", "harga", 
            "toko1", "alamat1", "toko2", "alamat2", 
            "toko3", "alamat3"
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter game name'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter release year'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input', 
                'rows': 3, 
                'placeholder': 'Enter game description'
            }),
            'developer': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter developer name'
            }),
            'genre': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter game genre'
            }),
            'ratings': forms.NumberInput(attrs={
                'class': 'form-input', 
                'step': 0.1, 'min': 0, 'max': 5,
                'placeholder': 'Enter ratings (0-5)'
            }),
            'harga': forms.NumberInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter price in IDR'
            }),
            'toko1': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter first store'
            }),
            'alamat1': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter address of first store'
            }),
            'toko2': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter second store (optional)'
            }),
            'alamat2': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter address of second store (optional)'
            }),
            'toko3': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter third store (optional)'
            }),
            'alamat3': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Enter address of third store (optional)'
            }),
        }
