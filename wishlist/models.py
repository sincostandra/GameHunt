from django.db import models
from django.contrib.auth.models import User
import uuid
from search.models import Game  # Ensure this import is correct

# Create your models here.
class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ratings = models.FloatField()

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey('search.Game', on_delete=models.CASCADE)  # Ensure the correct app label
    user = models.ForeignKey(User, on_delete=models.CASCADE)