from django.shortcuts import render
from .models import *
from .serializers import *


from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


# Create your views here.
@api_view(['POST'])        
def receiveData(request):
    
    device = {
    'serNo': data['SerNo'],
    'imei': data['IMEI'],
    'iccid': data['ICCID'],
    'prodId': data['ProdId'],
    'fw': data['FW'],
    }

    records = data['Records']

    for record in records:
        if record['Fields']:
            gps_data = record['Fields'][0]
            analogue_data = record['Fields'][2]['AnalogueData']
            record_sample = {
                "serNo": device['serNo'],   #Device foreignkey
                "seqNo": record['SeqNo'],   #Record sequence number
                "reason": record['Reason'],
                "dateUTC": record['DateUTC'],
                "lat": gps_data['Lat'],
                "long": gps_data['Long'],
                "alt": gps_data['Alt'],
                "voltage": analogue_data['1'],
                "temp": analogue_data['3'],
            }
    
    return Response()




@api_view(['POST'])        
def receiveDatabueno(request):
    print(request.data)
    serializer = ReceivedDataSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.validated_data) 
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)