from django.db import models
from django.contrib.auth.models import AbstractUser

class Senator(models.Model):
    senate_id = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    party = models.CharField(max_length=5)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    def __str__(self):
        return self.first_name + " " + self.last_name

class User(AbstractUser):
    email = models.EmailField(max_length=250, unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []