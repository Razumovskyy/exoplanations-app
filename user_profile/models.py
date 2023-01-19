from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    
    def __str__(self):
        return self.title
