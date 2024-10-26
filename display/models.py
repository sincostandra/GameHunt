from django.db import models
from search.models import Game
import uuid
 
class Comment(models.Model):
    game = models.ForeignKey(Game, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.game)