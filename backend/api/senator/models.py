# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Senator(models.Model):
    senate_id = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    party = models.CharField(max_length=5)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    # state = models.CharField(max_length=250)
    # in_office = models.BooleanField()
    # website = models.CharField(max_length=250)
    # contact_form = models.CharField(max_length=250 default=null)
    # twitter = models.CharField(max_length=250)
    # facebook = models.CharField(max_length=250)
    # youtube = models.CharField(max_length=250)
    # next_election = models.CharField(max_length=250)
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