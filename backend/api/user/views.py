from __future__ import unicode_literals
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from .models import User
# Create your views here.

# Users view
@api_view(['GET'])
def Users(request):
    users = User.objects.all()
    return Response(users)