from django.urls import path    
from review.views import show_reviews, show_json, get_review_json, create_review_ajax, edit_review, remove_ajax, get_user_review
from review.views import login_user, register, ooo

app_name = 'review'

urlpatterns = [
    path('show_reviews/<uuid:game_id>', show_reviews, name='show_reviews'),
    path('json/', show_json, name='show_json'),
    path('get_review_json/<uuid:game_id>', get_review_json, name='get_review_json'),
    path('create_review_ajax/<uuid:game_id>', create_review_ajax, name='create_review_ajax'),
    path('edit_reiew', edit_review, name='edit_review'),
    path('remove_ajax', remove_ajax, name='remove_ajax'),
    path('get_user_review/<uuid:game_id>', get_user_review, name='get_user_review'),

    path('ooo', ooo, name='ooo'),
    path('login/', login_user, name='login'),
    path('register/', register, name='logout'),
]