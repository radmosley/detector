from rest_framework import serializers
from .models import User, Senator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class SenatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Senator
        fields = '__all__'