from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_admin_user(sender, **kwargs):
    # Cek apakah user admin sudah ada
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', password='password123')
        print('Admin user created!')