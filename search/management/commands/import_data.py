from django.core.management.base import BaseCommand
import pandas as pd
from search.models import Game  # Pastikan model Game diimpor dengan benar
import re
class Command(BaseCommand):
    help = 'Import data from an Excel file into the Game model'

    def handle(self, *args, **kwargs):
        file_path = 'static/dataset/game_dataset.xlsx'  # Sesuaikan path file Excel
        df = pd.read_excel(file_path)

        for _, row in df.iterrows():
            harga_cleaned = int(re.sub(r'[^\d]', '', str(row['harga'])))
            Game.objects.create(
                name=row['name'],
                year=row['year'],
                description=row['description'],
                developer=row['developer'],
                genre=row['genre'],
                ratings=row['ratings'],
                harga=harga_cleaned,
                toko1=row['toko_1'],
                alamat1=row['alamat_1'],
                toko2=row.get('toko_2', ''),  # Optional field with a default empty string if not present
                alamat2=row.get('alamat_2', ''),  # Optional field with a default empty string if not present
                toko3=row.get('toko_3', ''),  # Optional field with a default empty string if not present
                alamat3=row.get('alamat_3', ''),  # Optional field with a default empty string if not present
            )
        self.stdout.write(self.style.SUCCESS('Data import completed successfully!'))
