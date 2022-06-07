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
        'SerNo': request.data['SerNo'],
        'IMEI': request.data['IMEI'],
        'ICCID': request.data['ICCID'],
        'ProdId': request.data['ProdId'],
        'FW': request.data['FW'],
    }
    records = dict(request.data['Records'][0])
    print('Hay ', len(records), '  records')
    #for i in range(len(records)):
    print(records)
        
        #if(len(records['Fields']) > 0):
            #gps_data = records[i]['Fields'][0]
            #analogue_data = records[i]['Fields'][2]
            #print(gps_data)
    
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