from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    developer = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    ratings = models.FloatField()
    harga = models.IntegerField()

    # Nama dan alamat toko
    toko1 = models.CharField(max_length=255)  # Wajib
    alamat1 = models.CharField(max_length=255)  # Wajib
    toko2 = models.CharField(max_length=255, null=True, blank=True)  # Optional
    alamat2 = models.CharField(max_length=255, null=True, blank=True)  # Optional
    toko3 = models.CharField(max_length=255, null=True, blank=True)  # Optional
    alamat3 = models.CharField(max_length=255, null=True, blank=True)  # Optional
