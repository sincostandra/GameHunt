from django.db import models
from django.contrib.auth.models import User
import uuid
from search.models import Game 

# Create your models here.
class Wishlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)  
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.user.username}'s Wishlist - {self.game.name}"
