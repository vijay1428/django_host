from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    email = models.EmailField(blank=False, max_length=254, verbose_name="email address")
    role = models.CharField(max_length=256, blank=True)
    roleStatus = models.CharField(max_length=256, blank=True)
    runnerId = models.CharField(max_length=256, blank=True)
    floaterId = models.CharField(max_length=256, blank=True)
    lastUpdate =models.DateTimeField(auto_now=True, blank=True)

    USERNAME_FIELD = "username"   # e.g: "username", "email"
    EMAIL_FIELD = "email"         # e.g: "email", "primary_email"

class ViewerDevice(models.Model):
    deviceId= models.CharField(max_length=256, blank=True)
    runnerUnit_limit_switch= models.CharField(max_length=256, blank=True)
    runnerUnitRelay_1= models.CharField(max_length=256, blank=True)
    runnerUnitRelay_2= models.CharField(max_length=256, blank=True)
    runnerUnitRelay_3= models.CharField(max_length=256, blank=True)
    runnerUnitDistance= models.CharField(max_length=256, blank=True)
    floaterUnit_limit_switch= models.CharField(max_length=256, blank=True)
    floaterUnitRelay_1= models.CharField(max_length=256, blank=True)
    floaterUnitRelay_2= models.CharField(max_length=256, blank=True)
    floaterUnitRelay_3= models.CharField(max_length=256, blank=True)
    floaterUnitDistance= models.CharField(max_length=256, blank=True)
    status = models.CharField(max_length=256, blank=True)
    notification = models.CharField(max_length=256, blank=True)
    error = models.CharField(max_length=256, blank=True)
    lastUpdate =models.DateTimeField(auto_now=True, blank=True) 

class RunnerUnitDetails(models.Model):
    deviceId= models.CharField(max_length=256, blank=True)
    status = models.CharField(max_length=256, blank=True)
    lastUpdate =models.DateTimeField(auto_now=True, blank=True) 

class CatalogDetails(models.Model):
    user_email = models.CharField(max_length=256, blank=True)
    catalogId= models.CharField(max_length=256, blank=True)
    status = models.CharField(max_length=256, blank=True)
    lastUpdate =models.DateTimeField(auto_now=True, blank=True)     

class FloaterUnitDetails(models.Model):
    deviceId= models.CharField(max_length=256, blank=True)
    status = models.CharField(max_length=256, blank=True)
    lastUpdate =models.DateTimeField(auto_now=True, blank=True)     


    
class UserProfileDetails(models.Model):
    pathName = models.CharField(max_length=256, blank=True)
    component = models.CharField(max_length=256, blank=True)
    fileName = models.CharField(max_length=256, blank=True)
    imagePath = models.CharField(max_length=256, blank=True)
    status = models.CharField(max_length=256, blank=True)
    lastUpdate =models.DateTimeField(auto_now=True, blank=True) 
    

class ReportUpdate(models.Model):
    user_email = models.CharField(max_length=256, blank=True)
    name = models.CharField(max_length=256, blank=True)
    description  = models.CharField(max_length=550, blank=True)
    location = models.FileField(upload_to='Report', max_length=1000)
    status = models.CharField(max_length=256, blank=True)
    lastUpdate =models.DateTimeField(auto_now=True, blank=True)

    
     
    
    


  


  
 




        

 
        
    