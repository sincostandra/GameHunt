from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
import uuid

class Game(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)  
    name = models.CharField(max_length=255)
    year = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    developer = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    ratings = models.FloatField()

    toko1 = models.CharField(max_length=255)  # Wajib
    alamat1 = models.CharField(max_length=255)  # Wajib
    toko2 = models.CharField(max_length=255, null=True, blank=True)  # Optional
    alamat2 = models.CharField(max_length=255, null=True, blank=True)  # Optional
    toko3 = models.CharField(max_length=255, null=True, blank=True)  # Optional
    alamat3 = models.CharField(max_length=255, null=True, blank=True)  # Optional

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'game')  # Pastikan tidak ada duplikasi game di wishlist

    def __str__(self):
        return f"{self.user.username}'s wishlist - {self.game.name}"

