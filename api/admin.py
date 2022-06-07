from django.contrib.admin import ModelAdmin, register
from .models import *

# Register your models here.
@register(ReceivedData)
class ReceivedDataAdmin(ModelAdmin):
    list_display = ['id','parsed',]