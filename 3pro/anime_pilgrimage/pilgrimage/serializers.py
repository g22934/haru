# pilgrimage/serializers.py
from rest_framework import serializers
from .models import PilgrimageLocation

class PilgrimageLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PilgrimageLocation
        fields = ['id', 'name', 'address', 'image']
