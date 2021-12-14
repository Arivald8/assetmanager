from rest_framework import serializers
from .models import Asset

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = [
            'device_name',
            'device_type',
            'device_asset',
            'device_serial',
            'device_model',
            'device_location',
            'device_ip',
            'device_mac',
            'device_school',
            'device_notes',
        ]
