from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


## CONNECTOR POST VIEW
@api_view(['POST'])        
def receiveData(request):
    
    errors = {
        'device': 'No errors',
        'record': 'No errors',     
    }

    device = {
    'serNo': request.data['SerNo'],
    'imei': request.data['IMEI'],
    'iccid': request.data['ICCID'],
    'prodId': request.data['ProdId'],
    'fw': request.data['FW'],
    }
    device_serializer = DeviceSerializer(data = device)
    if(device_serializer.is_valid()):
        device_serializer.save()
    else:
        errors['device'] = device_serializer.errors

    records = request.data['Records']

    for record in records:
        if record['Fields']:
            gps_data = record['Fields'][0]
            analogue_data = record['Fields'][2]['AnalogueData']
            record_sample = {
                "device": device['serNo'],   #Device foreignkey
                "seqNo": record['SeqNo'],   #Record sequence number
                "reason": record['Reason'],
                "dateUTC": record['DateUTC'],
                "lat": gps_data['Lat'],
                "long": gps_data['Long'],
                "alt": gps_data['Alt'],
                "voltage": analogue_data['1'],
                "temp": analogue_data['3'],
            }
            record_serializer = RecordSerializer(data = record_sample)
            if(record_serializer.is_valid()):
                record_serializer.save()
            else:
                errors['record'] = record_serializer.errors

    return Response(errors, status=status.HTTP_201_CREATED)



#
@api_view(['GET'])        
def devices(request):
    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many = True)
    return Response(serializer.data)

@api_view(['GET'])        
def records(request):
    records = Record.objects.all()
    serializer = RecordSerializer(records, many = True)
    return Response(serializer.data)