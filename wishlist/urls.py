from django.urls import path
from wishlist.views import view_wishlist, delete_wishlist
from .views import show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', view_wishlist, name='view_wishlist'),
    path('<int:id>/delete/', delete_wishlist, name='delete_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
