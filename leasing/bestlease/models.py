from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class register(models.Model):
    Name = models.CharField(max_length=30,blank=False, null=False)
    Phone_number = models.CharField(max_length=30,blank=False, null=False)
    Country = models.CharField(max_length=30,blank=False, null=False)
    Email_id = models.CharField(max_length=40,blank=False, null=False)
    Username = models.CharField(max_length=30,blank=False, null=False)
    Password = models.CharField(max_length=10,blank=False, null=False)
    Status = models.BooleanField(default=False)

class lessor(models.Model):
    Name = models.CharField(max_length=30)
    Phone_number = models.CharField(max_length=30)
    Company_name = models.CharField(max_length=30)
    Country = models.CharField(max_length=30)
    Email_id = models.CharField(max_length=40)
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=10)
    Status = models.BooleanField(default=False)

class upload(models.Model):
    Name = models.CharField(max_length=40,null=True)
    Container_id= models.CharField(max_length=40,null=True)
    Rate = models.CharField(max_length=40,null=True)
    Container_type = models.CharField(max_length=40,null=True)
    Container_length = models.CharField(max_length=40,null=True)
    Container_material= models.CharField(max_length=40,null=True)
    Container_condition = models.CharField(max_length=40,null=True)
    Location = models.CharField(max_length=100,null=True)
    Description = models.TextField(max_length=500,null=True)
    Picture = models.FileField(null=True)
    Owner = models.TextField(max_length=40,null=True)
    Status = models.BooleanField(default=False)

class book(models.Model):
    Name = models.CharField(max_length=40,null=True)
    Company_name= models.CharField(max_length=40,null=True)
    Company_address = models.CharField(max_length=100,null=True)
    Shipping_location = models.CharField(max_length=100,null=True)
    Phone_no = models.CharField(max_length=40,null=True)
    Email= models.CharField(max_length=40,null=True)
    Owner = models.TextField(max_length=40,null=True)
    Container_id = models.CharField(max_length=100,null=True)
    Status = models.BooleanField(default=False)
