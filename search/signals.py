from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command
from django.db import connection
from search.models import Game
from django.db import models

class DataImportStatus(models.Model):
    imported = models.BooleanField(default=False)

@receiver(post_migrate)
def import_data_after_migration(sender, **kwargs):
    if 'search_game' in connection.introspection.table_names():
        # Periksa apakah data sudah diimpor menggunakan DataImportStatus
        import_status, created = DataImportStatus.objects.get_or_create(id=1)

        if not import_status.imported:
            # Hanya jalankan import_data jika belum pernah diimpor sebelumnya
            print("Importing data...")
            call_command('import_data')
            print("Data import completed successfully!")
            
            # Update status menjadi sudah diimpor
            import_status.imported = True
            import_status.save()
        else:
            print("Data has already been imported, skipping import.")
