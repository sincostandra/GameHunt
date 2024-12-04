from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('login', login_user, name='login'),
    path('register', register_user, name='register'),
    path('logout', logout_user, name='logout'),
    path('flutter-login/', login_flutter, name='flutter_login'),
    path('flutter-register/', register_flutter, name='flutter_register'),
    path('flutter-logout/', logout_flutter, name='flutter_logout'),
]