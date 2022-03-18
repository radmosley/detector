from django.shortcuts import render
from .models import Senator
from rest_framework.response import Response
from .serializers import SenatorSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@api_view(['GET'])
def Senators(request):
    senators = Senator.objects.all()
    serializers = SenatorSerializer(senators, many=True)
    return Response(serializers.data,)