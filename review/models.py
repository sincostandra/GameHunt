from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# from search.game import Game
class Review(models.Model):
    judul_review = models.CharField(max_length=255)
    teks_review = models.TextField()
    nilai_review = models.IntegerField()
    pengguna = models.ForeignKey(User, on_delete=models.CASCADE)
    # game = models.ForeignKey(Game, on_delete=models.CASCADE)
    tanggal_review = models.DateTimeField(auto_now_add=True)
