from rest_framework import serializers
from .models import Senator
import io
import json


class SenatorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=250)
    last_name = serializers.CharField(max_length=250)

    def create(self, validated_data):
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)
        return Senator.objects(**validated_data)
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.save()
        return instance