# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
# Senator view
@api_view(['GET'])
def Senators(request):
    return Response('hello')