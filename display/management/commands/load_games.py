import csv
import os
from django.core.management.base import BaseCommand
from display.models import Game
from django.conf import settings

class Command(BaseCommand):
    help = 'Load game data from CSV file'

    def handle(self, *args, **kwargs):
        # Construct the full path to the CSV file
        csv_file_path = os.path.join(settings.BASE_DIR, 'display', 'data', 'games_dataset.csv')
        
        with open(csv_file_path, newline='',encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Game.objects.create(
                    name=row['name'],
                    year=row['year'],
                    description=row['description'],
                    developer=row['developer'],
                    genre=row['genre'],
                    ratings=row['ratings'],
                    harga=row['harga'],
                    toko1=row['toko_1'],
                    alamat1=row['alamat_1'],
                    toko2=row['toko_2'],
                    alamat2=row['alamat_2'],
                    toko3=row['toko_3'],
                    alamat3=row['alamat_3']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded game data'))
