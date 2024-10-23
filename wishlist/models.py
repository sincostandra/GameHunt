from django.db import models

# Create your models here.
# models.py

from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    description = models.TextField()
    developer = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'game')  # Pastikan tidak ada duplikasi game di wishlist

    def __str__(self):
        return f"{self.user.username}'s wishlist - {self.game.name}"

