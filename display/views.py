from uuid import UUID
from django.shortcuts import get_object_or_404, render
from display.models import Comment
from display.forms import CommentForm
from search.models import Game
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.utils.html import strip_tags
from django.contrib import messages
import json

# Create your views here.
def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})

def game_detail(request, id):
    game=Game.objects.get(pk=id)
    comments = Comment.objects.filter(game=game).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            body = request.POST.get('body')
            comment = Comment.objects.create(game=game, name=request.user.username, body=body)
            comment.save()
            return HttpResponseRedirect(reverse('display:game_detail', args=[id]))
    else:
        comment_form = CommentForm()

    context = {'game': game, 
               'comments': comments, 
               'comment_form': comment_form}

    return render(request, 'game_detail.html', context)

def show_json_by_id(request, id):
    game = Game.objects.get(pk=id)
    data = Comment.objects.filter(game=game)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def json_allcomments(request):
    data = Comment.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
@require_POST
def add_comment_ajax(request, id):
    # Extract the comment body from the POST request
    body = request.POST.get("body")
    name = request.user.username
    game = Game.objects.get(pk=id)
    created = timezone.now()
    formatted_created = created.strftime("%B %d, %Y, %I:%M %p")
    
    # Create a new Comment object and save it to the database
    new_comment = Comment(
        game=game,
        body=body, 
        name=name,
        created=formatted_created
    )
    new_comment.save()

    return HttpResponse(b"CREATED", status=201)

def delete_comment(request, id):
    # Get game berdasarkan id
    comment = Comment.objects.get(pk=id)
    # Hapus game
    comment.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('display:game_detail', args=[comment.game.id]))

@csrf_exempt
def create_comment_flutter(request):   
    if request.method == 'POST':

        data = json.loads(request.body)
        new_comment = Comment.objects.create(
            name=request.user.username,
            body=data['body'],
            game=Game.objects.get(pk=data['game']),
            created=timezone.now()
        )

        new_comment.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def delete_comment_flutter(request, id):
    if request.method == 'DELETE':
        try:
            # news_uuid = UUID(news_id)
            comment = Comment.objects.get(pk=id)
            comment.delete()
            return JsonResponse({"status": "success"}, status=200)
        except Comment.DoesNotExist:
            return JsonResponse({"status": "error", "message": "News not found"}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)