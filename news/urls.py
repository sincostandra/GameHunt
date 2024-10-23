from django.urls import path
from .views import show_main
from .views import show_news, edit_news, create_news, home_news, delete_news

app_name = 'main'

urlpatterns = [
    path('news', home_news, name='home_news'),
    path('news/<uuid:id>', show_news, name='create_news'),
    path('create-news/<uuid:id>', create_news, name='create_news'),
    path('edit-news/<uuid:id>', edit_news, name='edit_news'),
    path('delete/<uuid:id>', delete_news, name='delete_news'),
]