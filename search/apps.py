<<<<<<< HEAD
from django.apps import AppConfig


class SearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'search'
=======
# search/apps.py
from django.apps import AppConfig

class SearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'search'

    def ready(self):
        import search.signals  # Pastikan ini diimport saat app siap
>>>>>>> 320f02c7688d29fe78f1f4130ecbf852bcb527d3
