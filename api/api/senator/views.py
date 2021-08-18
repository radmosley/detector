from django.conf.urls import url
from api.senator.models import Senator
from rest_framework import viewsets
from api.senator.serializers import SenatorSerializer

# Create your views here.
class SenatorViewSet(viewsets.ModelViewSet):
    queryset = Senator.objects.all()
    serializer_class = SenatorSerializer
