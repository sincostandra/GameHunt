from django.db import models
import uuid

# Create your models here.

class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    title = models.CharField(max_length=255)
    article = models.TextField()
    author = models.CharField(max_length=255)
    # Automatically sets the creation date
    # post_date = models.DateTimeField(auto_now_add=True)
    # Automatically updates the field on each save
    update_date = models.DateTimeField(auto_now=True)

    
