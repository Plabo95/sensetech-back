from django.db import models
from django.db.models import *

# Create your models here.
class ReceivedData(models.Model):
    headers = JSONField(default=dict, null=True, blank=True)
    data = JSONField(default=dict, null=True, blank=True)
    parsed = models.BooleanField(default=True)
    parsing_message = models.TextField(default="Parsed Correctly")

    def __str__(self):
        return('Received data ok!')