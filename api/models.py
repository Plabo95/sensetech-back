from django.db import models
from django.db.models import *


class Device(models.Model):
    name = models.CharField(("name"),max_length=255,)
    serNo = models.CharField(("serial number"),max_length=255,help_text=("Device serial number"),unique=True,primary_key=True)
    iccid = models.CharField(("SIM serial number"),max_length=255,help_text=("SIM serial number"),)
    imei = models.CharField(("Modem IMEI"),max_length=255,help_text=("Modem IMEI"),)
    prodId = models.CharField(("Product TYPE/ID"),max_length=255,help_text=("Product ID"),)
    fw = models.CharField(("Firmware version"),max_length=255,help_text=("Firmware version"),)

class Record(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE )
    seqNo = models.CharField(max_length=255, help_text=("Record sequence number"))
    reason = models.CharField(max_length=255, help_text=("Reason for logging record"))
    dateUTC = models.DateTimeField(max_length=255, help_text=("Device UTC datetime"))
    lat = models.DecimalField(("latitude"),max_digits=12,decimal_places=7,help_text=("Latitude"))
    long =  models.DecimalField(("longitude"),max_digits=12,decimal_places=7,help_text=("Longitude"))
    alt= models.IntegerField(("altitude"), help_text=("Altitude"))
    voltage = models.DecimalField(("voltage"),help_text=("Battery Voltage in mV "),max_digits=7,decimal_places=3,)
    temp = models.DecimalField(("temperature"),help_text=("Temperature Deg C"),max_digits=7,decimal_places=3,)
