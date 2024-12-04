from django.shortcuts import render
from django.contrib import messages
from review.models import Review
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from review.forms import ReviewForm
from search.models import Game
# Create your views heresss.

# GET (Read)
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

# POST (Create) Ajax
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

# GET Json Data (all review of user)
def get_review_json(request, game_id):
    reviews = Review.objects.filter(game_id=game_id)\
        .annotate(
            vote_count=Count('upvotes') - Count('downvotes')
        )\
        .order_by('-vote_count', '-date')  # Sort by votes first, then by date
    
    return JsonResponse([{
        'id': review.id,
        'username': review.user.username,
        'title': review.title,
        'content': review.content,
        'score': review.score,
        'date': str(review.date)[:10] + " " + str(review.date)[11:20],
        'vote_score': review.vote_score,
        'user_upvoted': request.user in review.upvotes.all() if request.user.is_authenticated else False,
        'user_downvoted': request.user in review.downvotes.all() if request.user.is_authenticated else False
    } for review in reviews], safe=False)


# GET Json Data (specific one user)
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

# POST (Delete) Ajax
@csrf_exempt
def remove_ajax(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        data = Review.objects.get(pk=id)
        data.delete()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

# POST AND GET
@login_required
@csrf_exempt
def vote_review(request):
    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        vote_type = request.POST.get('vote_type')
        
        try:
            review = Review.objects.get(pk=review_id)
            user = request.user

            # Check if user is trying to cancel their vote
            if vote_type == 'upvote' and user in review.upvotes.all():
                review.upvotes.remove(user)  # Cancel upvote
            elif vote_type == 'downvote' and user in review.downvotes.all():
                review.downvotes.remove(user)  # Cancel downvote
            else:
                # Remove any existing votes first
                review.upvotes.remove(user)
                review.downvotes.remove(user)
                
                # Add new vote
                if vote_type == 'upvote':
                    review.upvotes.add(user)
                elif vote_type == 'downvote':
                    review.downvotes.add(user)

            return JsonResponse({
                'status': 'success',
                'vote_score': review.vote_score,
                'user_upvoted': user in review.upvotes.all(),
                'user_downvoted': user in review.downvotes.all()
            })
        except Review.DoesNotExist:
            return JsonResponse({'status': 'error'}, status=404)

    return JsonResponse({'status': 'error'}, status=400)