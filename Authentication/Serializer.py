from rest_framework import serializers
from .models import *
class AuthWindowStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthWindowStyle
        fields = '__all__'