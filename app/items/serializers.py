from django.db import models
from rest_framework import serializers
from core.models import Rack, Pdu 


class RackSerializer(serializers.ModelSerializer):
    """Serializer for rack objects"""
    class Meta:
        model = Rack
        fields = ('id', 'height', 'location', 'color', 'pdus')
        read_only_fields = ('id',)

class PduSerializer(serializers.ModelSerializer):
    """Serializer for pdu objects"""
    class Meta:
        model = Pdu
        fields = "__all__"