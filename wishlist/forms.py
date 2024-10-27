from django.forms import ModelForm
from django import forms
from .models import Wishlist
from django.utils.html import strip_tags

class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['game']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['game'].widget = forms.TextInput()