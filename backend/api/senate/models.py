from django.db import models

# Create your models here.
class Senator(models.Model):
    senate_id = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    party = models.CharField(max_length=5)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    def __str__(self):
        return "Sen" + self.first_name + " " + self.last_name