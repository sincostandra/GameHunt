from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"== UserProfile ==\n" \
               f"description : {self.description}\n" \
               f"first_name : {self.first_name}\n" \
               f"last_name : {self.last_name}\n" \
               f"date_of_birth : {self.date_of_birth}\n" \
               f"gender : {self.gender}\n" \
               f"location : {self.location}\n" \
               f"phone_number : {self.phone_number}\n" \
               f"email : {self.email}"