# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework import exceptions
from .serializers import UserSerializer, SenatorSerializer
from .models import Senator, User
# Create your views here.
# Senator view
# @api_view(['GET'])
# def Senator(request):
#     senators = Senator.objects.all()
#     return Response(senators)
# @api_view(['POST'])
def Register(request):
    data = request.data

    if data['password'] != data['password_confirm']:
        raise exceptions.APIException('Passwords do not match')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def Users(request):
    users = User.objects.all()
    serializers = UserSerializer(users, many=True)
    return Response(serializers.data,)

@api_view(['GET'])
def Senators(request):
    senators = Senator.objects.all()
    serializers = SenatorSerializer(senators, many=True)
    return Response(serializers.data,)