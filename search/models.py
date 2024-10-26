from django.db import models
import uuid

class Game(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)  
    name = models.CharField(max_length=255)
    year = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    developer = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    ratings = models.FloatField()
    harga = models.IntegerField()

    toko1 = models.CharField(max_length=255)  # Wajib
    alamat1 = models.CharField(max_length=255)  # Wajib
    toko2 = models.CharField(max_length=255, null=True, blank=True)  # Optional
    alamat2 = models.CharField(max_length=255, null=True, blank=True)  # Optional
    toko3 = models.CharField(max_length=255, null=True, blank=True)  # Optional
    alamat3 = models.CharField(max_length=255, null=True, blank=True)  # Optional

class DataImportStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    imported = models.BooleanField(default=False)
