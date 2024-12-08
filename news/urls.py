from django.urls import path
from .views import show_news, edit_news, create_news, home_news, delete_news
from .views import show_xml, show_json, show_xml_by_id, show_json_by_id
from .views import create_news_flutter

app_name = 'news'

urlpatterns = [
    path('', home_news, name='home_news'),
    path('<uuid:id>', show_news, name='show_news'),
    path('create-news/', create_news, name='create_news'),
    path('edit-news/<uuid:id>', edit_news, name='edit_news'),
    path('delete/<uuid:id>', delete_news, name='delete_news'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('create-flutter/', create_news_flutter, name='create_news_flutter'),
]