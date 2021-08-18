from django.db import models

class Senator(models.Model):
    first_name = models.CharField(max_length=200, default='First Name')
    last_name = models.CharField(max_length=200, default='Last Name')
    short_title = models.CharField(max_length=200, default='Senator')