# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Senator(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    # contact_form = models.URLField()
    # website = models.URLField()
    # state = models.CharField()
    # phone = models.CharField()
    # office = models.CharField()
    # next_election = models.CharField()
    # status = models.BooleanField()
    # party = models.CharField()
    def __str__(self):
        return self.first_name + " " + self.last_name 