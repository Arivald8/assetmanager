from django.db import models

class Asset(models.Model):
    device_name = models.CharField(max_length=45, blank=False)
    device_type = models.CharField(max_length=45)
    device_asset = models.CharField(max_length=45, unique=True)
    device_serial = models.CharField(max_length=45, unique=True)
    device_model = models.CharField(max_length=45)
    device_location = models.CharField(max_length=45)
    device_ip = models.CharField(max_length=45)
    device_mac = models.CharField(max_length=45)
    device_school = models.CharField(max_length=4)
    device_notes = models.CharField(max_length=100)
    
    class Meta:
        db_table = "all_devices"