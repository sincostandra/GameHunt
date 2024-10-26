from uuid import UUID
from django.shortcuts import get_object_or_404, render
from display.models import Comment
from display.forms import CommentForm
from search.models import Game
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.utils.html import strip_tags
from django.contrib import messages

# Create your views here.
def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})

def game_detail(request, id):
    game=Game.objects.get(pk=id)
    # comments = Comment.objects.filter(game=game).order_by('-id')
    print(game)

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
            #    'comments': comments, 
               'comment_form': comment_form}

    return render(request, 'game_detail.html', context)

def show_json_by_id(id):
    game = get_object_or_404(Game, id=id)
    data = Comment.objects.filter(game=game)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# @csrf_exempt
# @require_POST
# def add_comment_ajax(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         comment_body = data.get("body")  # Get the comment body from JSON
#         game_id = data.get('game_id')  # Ensure the game ID is passed as well
#         try:

#             # Fetch the game object; if it doesn't exist, raise an error
#             game = Game.objects.get(id=game_id)

#             # Create a new Comment object
#             new_comment = Comment(
#                 game=game,
#                 name=request.user.username,  # Use the logged-in user's name
#                 body=comment_body,
#                 created=timezone.now()
#             )
#             new_comment.save()  # Save the comment to the database

#             # Return a success response
#             return JsonResponse({"message": "Comment added successfully", "comment": comment_body}, status=201)
        
#         except Game.DoesNotExist:
#             # Handle the case where the game ID is invalid
#             return JsonResponse({"error": "Game not found."}, status=404)
#         except Exception as e:
#             # Catch any other exceptions and return a generic error message
#             return JsonResponse({"error": str(e)}, status=500)

#     # Return an error response for invalid requests
#     return JsonResponse({"error": "Invalid request method."}, status=400)

@csrf_exempt
@require_POST
def add_comment_ajax(request):
    body = strip_tags(request.POST.get("body"))
    user = request.user
    game = get_object_or_404(Game, id=id)
    created = timezone.now()

    new_comment = Comment(
        game=game,
        body=body, 
        user=user,
        created=created
    )

    if body == "":
        messages.error(request, "Please fill all the fields")
        return HttpResponse(b"BAD REQUEST", status=400)
    else:
        new_comment.save()

    return HttpResponse(b"CREATED", status=201)