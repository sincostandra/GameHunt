from django.urls import path    
from review.views import show_reviews, get_review_json, create_review_ajax, remove_ajax, get_user_review, vote_review, delete_review_flutter, get_user_role

app_name = 'review'

urlpatterns = [
    path('show_reviews/<uuid:game_id>', show_reviews, name='show_reviews'),
    path('get_review_json/<uuid:game_id>', get_review_json, name='get_review_json'),
    path('create_review_ajax/<uuid:game_id>', create_review_ajax, name='create_review_ajax'),
    path('remove_ajax', remove_ajax, name='remove_ajax'),
    path('get_user_review/<uuid:game_id>', get_user_review, name='get_user_review'),
    path('vote/', vote_review, name='vote_review'),
    path('delete_review_flutter/<int:id>/', delete_review_flutter, name='delete_review_flutter'),
    path('get_user_role', get_user_role, name='get_user_role')
]