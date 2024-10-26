import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.http import require_POST
from review.models import Review
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from search.models import Game
from django.contrib.auth.decorators import user_passes_test
# from books.models import Book
# from reviews.forms import ReviewForm

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from review.forms import ReviewForm
from search.models import Game
# Create your views here.

@login_required(login_url='review:login')
def show_reviews(request, game_id):
    game = Game.objects.get(pk=game_id)
    reviews = Review.objects.filter(game=game)
    try:
        review_user = Review.objects.get(game=game, user=request.user)
        score = review_user.score
    except Review.DoesNotExist:
        review_user = None
        score = None

    context = {
        'reviews': reviews,
        'game': game,
        'game_id': game_id,
        'user': request.user,
        'username': request.user.username,
        'users': User.objects.all(),
        'score': score,
        'review_user': review_user
    }
    return render(request, 'reviews.html', context)

@csrf_exempt
@login_required
def create_review_ajax(request, game_id):
    if request.method == 'POST':
        game = Game.objects.get(pk=game_id)
        title = request.POST.get("title")
        score = request.POST.get("score")
        content = request.POST.get("content")

        review = Review.objects.create(
            title=title,
            score=score,
            content=content,
            game=game,
            user=request.user
        )

        # Return the created review data
        return JsonResponse({
            'title': review.title,
            'content': review.content,
            'score': review.score,
            'id': review.id,
            'username': request.user.username
        })

    return HttpResponseNotFound()

# Add a new view to get user's review

def get_review_json(request, game_id):
    reviews = Review.objects.filter(game_id=game_id)
    return JsonResponse([{
        'id': review.id,
        'username': review.user.username,
        'title': review.title,
        'content': review.content,
        'score': review.score
    } for review in reviews], safe=False)


@login_required
def get_user_review(request, game_id):
    game = Game.objects.get(pk=game_id)
    try:
        review = Review.objects.get(game=game, user=request.user)
        return JsonResponse({
            'title': review.title,
            'content': review.content,
            'score': review.score,
            'id': review.id,
            'username': request.user.username
        })
    except Review.DoesNotExist:
        return JsonResponse({}, status=404)

@csrf_exempt
def remove_ajax(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        data = Review.objects.get(pk=id)
        data.delete()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def edit_review(request, review_id, game_id):
    review = Review.objects.get(pk = review_id)

    form = ReviewForm(request.POST or None, instance=review)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('review:show_reviews', args=[game_id]))

    context = {'form': form}
    return render(request, "edit_review.html", context)

def show_json(request):
    data = Game.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@user_passes_test(lambda u: u.is_staff)
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return HttpResponse(b"CREATED", status=201)

### HAPUS KODE DI BAWAH !!!!!!!!

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('review:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return redirect('main:show_main')
            response = HttpResponseRedirect(reverse("review:ooo"))
            response.set_cookie('last_login')
            return response
      else:
          messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def ooo(request):
    return HttpResponse("Hello, world. You're at the ooo view.")