from .models import *
from rest_framework import serializers

class ReceivedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedData
        fields = '__all__'