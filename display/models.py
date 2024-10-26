from django.db import models
from search.models import Game
import uuid

# Create your models here.
# class Game(models.Model):
#     id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)  
#     name = models.CharField(max_length=255)
#     year = models.IntegerField(null=True, blank=True)
#     description = models.TextField()
#     developer = models.CharField(max_length=255)
#     genre = models.CharField(max_length=255)
#     ratings = models.FloatField()
#     harga = models.IntegerField()

#     toko1 = models.CharField(max_length=255)  # Wajib
#     alamat1 = models.CharField(max_length=255)  # Wajib
#     toko2 = models.CharField(max_length=255, null=True, blank=True)  # Optional
#     alamat2 = models.CharField(max_length=255, null=True, blank=True)  # Optional
#     toko3 = models.CharField(max_length=255, null=True, blank=True)  # Optional
#     alamat3 = models.CharField(max_length=255, null=True, blank=True)  # Optional

    # def __str__(self):
    #     return self.name
    
class Comment(models.Model):
    game = models.ForeignKey(Game, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.game)