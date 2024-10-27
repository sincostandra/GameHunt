import csv
import os
from django.core.management.base import BaseCommand
from news.models import News
from django.conf import settings

class Command(BaseCommand):
    help = 'Load news data from CSV file'

    def handle(self, *args, **kwargs):
        # Construct the full path to the CSV file
        csv_file_path = 'static/dataset/news_data.csv'
        
        with open(csv_file_path, newline='',encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                News.objects.create(
                    title=row['title'],
                    article=row['text'],
                    author=row['author'],
                    post_date=row['publish_date'],
                    update_date=row['publish_date'],
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded news data'))