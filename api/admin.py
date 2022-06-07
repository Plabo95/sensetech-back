from django.contrib.admin import ModelAdmin, register
from .models import *

# Register your models here.
@register(Device)
class DeviceAdmin(ModelAdmin):
    list_display = ['serNo',]

@register(Record)
class RecordAdmin(ModelAdmin):
    list_display = ['seqNo',]