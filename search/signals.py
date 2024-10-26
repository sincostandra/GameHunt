from django.db import connection
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command
from search.models import DataImportStatus

@receiver(post_migrate)
def import_data_after_migration(sender, **kwargs):
    # Pastikan tabel 'search_dataimportstatus' sudah ada sebelum mengaksesnya
    if 'search_dataimportstatus' in connection.introspection.table_names():
        import_status, created = DataImportStatus.objects.get_or_create(id=1)

        # Cek apakah ini adalah pertama kali atau belum pernah diimport
        if created or not import_status.imported:
            print("Importing data...")
            call_command('import_data')
            import_status.imported = True
            import_status.save()
            print("Data import completed successfully!")
    else:
        print("Table 'search_dataimportstatus' not found yet. Skipping data import.")
