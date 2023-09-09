import binascii
from datetime import datetime
import json
import os
from django.http import JsonResponse
from django.views import View
from rest_framework.viewsets import ModelViewSet

# from Backend1.vividobots.products.models import ReportUpdate

# from .settings import MEDIA_ROOT
from .serializers import CustomUserSerializer,ViewerDeviceSerializer,ReportUpdateSerializer
from products.models import CustomUser,ViewerDevice,ReportUpdate
from rest_framework.views import APIView
from rest_framework.response import Response
from graphene.relay.node import Node
import base64
from django.http import HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from PIL import Image
from rest_framework.permissions import AllowAny
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.core.files import File
from django.http import HttpResponse
from rest_framework.decorators import api_view

# from Backend.products.models import CustomUser
# from flask import Flask, request, jsonify
# import RPi.GPIO as GPIO

# app = Flask(__name__)





    
        


    

    
class DevicePostView(APIView):

    def get(self, request, id): 
        last_viewer_device = ViewerDevice.objects.filter(deviceId=id)
        filtered_numbers = [num for num in last_viewer_device]
        length_of_filtered_numbers = len(filtered_numbers)

        if length_of_filtered_numbers >= 1 :
            # last_viewer_device2 = ViewerDevice.objects.filter(deviceId=id).latest()
            last_viewer_device2 = ViewerDevice.objects.get(deviceId=id)
            last_viewer_device2.runnerUnit_limit_switch="false"
            last_viewer_device2.runnerUnitRelay_1="false"
            last_viewer_device2.runnerUnitRelay_2="false"
            last_viewer_device2.runnerUnitRelay_3="false"
            last_viewer_device2.runnerUnitDistance="0"
            last_viewer_device2.floaterUnit_limit_switch="false"
            last_viewer_device2.floaterUnitRelay_1="false"
            last_viewer_device2.floaterUnitRelay_2="false"
            last_viewer_device2.floaterUnitRelay_3="false"
            last_viewer_device2.floaterUnitDistance="0"
            last_viewer_device2.status="true"
            last_viewer_device2.save()

        else : 
         
            data = ViewerDevice.objects.create( deviceId=id,
                                               runnerUnit_limit_switch="false",
                                               runnerUnitRelay_1="false",
                                               runnerUnitRelay_2="false",
                                               runnerUnitRelay_3="false",
                                               runnerUnitDistance="0",
                                               floaterUnit_limit_switch="false",
                                               floaterUnitRelay_1="false",
                                               floaterUnitRelay_2="false",
                                               floaterUnitRelay_3="false",
                                               floaterUnitDistance="0",
                                               status="true")
            data.save()
            print("b")

        qs1 = ViewerDevice.objects.get(deviceId=id)
        serializer = ViewerDeviceSerializer(qs1)  # Serialize the queryset
        return Response(serializer.data)
    
        # return HttpResponse("Active") 
    
class DeviceStopPostView(APIView):

    def get(self, request, id): 
        last_viewer_device2 = ViewerDevice.objects.get(deviceId=id)
           
        last_viewer_device2.status="false"
        last_viewer_device2.save()
        qs1 = ViewerDevice.objects.get(deviceId=id)
        serializer = ViewerDeviceSerializer(qs1)  # Serialize the queryset
        return Response(serializer.data)    


class DeviceStateGetView(APIView):
    def get(self, request, id):
        # _, file_pk = Node.from_global_id(id)
        qs1 = ViewerDevice.objects.get(deviceId=id)
        serializer = ViewerDeviceSerializer(qs1)  # Serialize the queryset
        data = serializer.data
        id_value = data['status']
        print(id)
        print( id_value)
        if id_value == 'true':
          
          return Response(1)
        else :
            return Response(0)
        
class DeviceRunnerUnitLimitSwitchView(APIView):

    def get(self, request, id,status): 
        last_viewer_device2 = ViewerDevice.objects.get(deviceId=id)
        print(id,status)  
        last_viewer_device2.runnerUnit_limit_switch=status
        last_viewer_device2.save()
        qs1 = ViewerDevice.objects.get(deviceId=id)
        serializer = ViewerDeviceSerializer(qs1)
        id_value = serializer.data['runnerUnit_limit_switch']
        if id_value == 'true':
          
          return Response(1)
        else :
            return Response(0)  

class DeviceFloaterUnitLimitSwitchView(APIView):

    def get(self, request, id,status): 
        last_viewer_device2 = ViewerDevice.objects.get(deviceId=id)
        print(id,status)  
        last_viewer_device2.floaterUnit_limit_switch=status
        last_viewer_device2.save()
        qs1 = ViewerDevice.objects.get(deviceId=id)
        serializer = ViewerDeviceSerializer(qs1)
        id_value = serializer.data['floaterUnit_limit_switch']
        if id_value == 'true':
          
          return Response(1)
        else :
            return Response(0)                 
        
class DevicerunnerUnitLimitSwitchStateGetView(APIView):
    def get(self, request, id):
        # _, file_pk = Node.from_global_id(id)
        qs1 = ViewerDevice.objects.get(deviceId=id)
        serializer = ViewerDeviceSerializer(qs1)  # Serialize the queryset
        data = serializer.data
        value = data['runnerUnit_limit_switch']
        print(id)
        print(value)
        if value == 'true':
          
          return Response(1)
        else :
            return Response(0)        

class DevicefloaterUnitLimitSwitchStateGetView(APIView):
    def get(self, request, id):
        # _, file_pk = Node.from_global_id(id)
        qs1 = ViewerDevice.objects.get(deviceId=id)
        serializer = ViewerDeviceSerializer(qs1)  # Serialize the queryset
        data = serializer.data
        value = data['floaterUnit_limit_switch']
        print(id)
        print(value)
        if value == 'true':
          
          return Response(1)
        else :
            return Response(0) 
        
class DeviceRunnerUnitRelay_1View(APIView):

    def get(self, request, id,status): 
        last_viewer_device2 = ViewerDevice.objects.get(deviceId=id)
        print(id,status)  
        last_viewer_device2.runnerUnitRelay_1=status
        last_viewer_device2.save()
        qs1 = ViewerDevice.objects.get(deviceId=id)
        serializer = ViewerDeviceSerializer(qs1)
        id_value = serializer.data['runnerUnitRelay_1']
        if id_value == 'true':
          
          return Response(1)
        else :
            return Response(0)
       
class DeviceRunnerUnitRelay_2View(APIView):

    def get(self, request, id,status): 
        last_viewer_device2 = ViewerDevice.objects.get(deviceId=id)
        print(id,status)  
        last_viewer_device2.runnerUnitRelay_2=status
        last_viewer_device2.save()
        qs1 = ViewerDevice.objects.get(deviceId=id)
        serializer = ViewerDeviceSerializer(qs1)
        id_value = serializer.data['runnerUnitRelay_2']
        if id_value == 'true':
          
          return Response(1)
        else :
            return Response(0)      

class DeviceRunnerUnitRelay_3View(APIView):

    def get(self, request, id,status): 
        last_viewer_device2 = ViewerDevice.objects.get(deviceId=id)
        print(id,status)  
        last_viewer_device2.runnerUnitRelay_3=status
        last_viewer_device2.save()
        qs1 = ViewerDevice.objects.get(deviceId=id)
        serializer = ViewerDeviceSerializer(qs1)
        id_value = serializer.data['runnerUnitRelay_3']
        if id_value == 'true':
          
          return Response(1)
        else :
            return Response(0)          
    

class DeviceRunnerUnitDistanceView(APIView):

    def get(self, request, id,status): 
        last_viewer_device2 = ViewerDevice.objects.get(deviceId=id)
        print(id,status)  
        last_viewer_device2.runnerUnitDistance=status
        last_viewer_device2.save()
        qs1 = ViewerDevice.objects.get(deviceId=id)
        serializer = ViewerDeviceSerializer(qs1)
        id_value = serializer.data['runnerUnitDistance']
        return Response( id_value)
         


class DeviceNotificationView(APIView):

    def get(self, request, id,status): 
        last_viewer_device2 = ViewerDevice.objects.get(deviceId=id)
        print(id,status)  
        last_viewer_device2.runnerUnitDistance=status
        last_viewer_device2.save()
        qs1 = ViewerDevice.objects.get(deviceId=id)
        serializer = ViewerDeviceSerializer(qs1)
        id_value = serializer.data['notification']
        return Response( id_value)

# class GenerateReportView(APIView):

#     def get(self, request, id,status): 

#         print(id,status)  
        
#         return Response( id)         
     


class GenerateReportView(APIView):

    def post(self, request): 
        folder_name = './Uploaded_image/'
        # file_name = 'Product/'+id+'.png'

        path_to_file = folder_name + 'filename.pdf'
        # f = open(path_to_file, 'rb')
        # pdfFile = File(f)
        # response = HttpResponse(pdfFile.read())
        # response['Content-Disposition'] = 'attachment'
        return Response (path_to_file)

class ReportUpdateViewSet(ModelViewSet):
    queryset = ReportUpdate.objects.all()
    serializer_class = ReportUpdateSerializer


 
    
    
    

    
    
