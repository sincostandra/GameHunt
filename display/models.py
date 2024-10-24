from django.db import models
import uuid

# Create your models here.
class Game(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)  
    name = models.CharField(max_length=255)
    year = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    developer = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    ratings = models.FloatField()
    harga = models.IntegerField()

    def __str__(self):
        return self.name