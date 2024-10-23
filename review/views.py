import json
from django.shortcuts import render
from review.models import review 

from review.models import Review
# from search.models import Game

# from books.models import Book
# from reviews.forms import ReviewForm

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
# Create your views here.

@login_required(login_url='main:login')
def show_reviews(request, game_id):
    game = Game.objects.get(pk=game_id)
    