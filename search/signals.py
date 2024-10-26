# search/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command
from django.db import connection

@receiver(post_migrate)
def import_data_after_migration(sender, **kwargs):
    if 'search_game' in connection.introspection.table_names():
        print("Importing data...")
        call_command('import_data')
