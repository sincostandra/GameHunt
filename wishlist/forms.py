from django.forms import ModelForm
from django import forms
from .models import Wishlist
from django.utils.html import strip_tags

class WishlistForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['game']