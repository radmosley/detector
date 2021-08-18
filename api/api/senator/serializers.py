from rest_framework import serializers
from api.senator.models import Senator


class SenatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Senator
        fields = ['url', 'username', 'email', 'grou']