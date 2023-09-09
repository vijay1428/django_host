# from rest_framework import serializers

from rest_framework import serializers
from products.models import CustomUser,ViewerDevice,ReportUpdate
# from .models import   # Import your CustomUser model

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'  # You can specify the fields you want to include

class ViewerDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewerDevice
        fields = '__all__'  # You can specify the fields you want to include
        
class ReportUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportUpdate
        fields = '__all__'  # You can specify the fields you want to include       