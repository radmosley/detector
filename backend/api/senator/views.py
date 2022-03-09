# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .authentication import generate_access_token
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import exceptions
from .serializers import UserSerializer, SenatorSerializer
from .models import Senator, User
# Create your views here.
# Senator view
# @api_view(['GET'])
# def Senator(request):
#     senators = Senator.objects.all()
#     return Response(senators)
@api_view(['POST'])
def Register(request):
    data = request.data

    if data['password'] != data['password_confirm']:
        raise exceptions.APIException('Passwords do not match')

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def Login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    user = User.objects.filter(email=email).first()

    if user is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if not user.check_password(password):
        raise exceptions.AuthenticationFailed("Incorrect password")
    response = Response()
    token = generate_access_token(user)
    response.set_cookie(key="JWT", value=token, httponly=True)
    response.data = {
        "jwt": token
    }
    return response

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