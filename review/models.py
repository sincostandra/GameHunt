from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from search.models import Game

# Model Init review
class Review(models.Model):

    game = models.ForeignKey(Game, on_delete=models.CASCADE,  related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='review_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='review_downvotes', blank=True)

    @property
    def vote_score(self):
        return self.upvotes.count() - self.downvotes.count()
