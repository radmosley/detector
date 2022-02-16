# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Senator(models.Model):
    first_name = models.Charfield(maxlength=250)
    last_name = models.Charfield(maxlength=250)
    def __str__(self):
        return self.first_name + " " + self.last_name 