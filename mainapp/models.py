from django.db import models
from django.utils import timezone

# Create your models here.
class User_Model(models.Model):
    user_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50)
    password = models.TextField(max_length=50)
    email = models.EmailField(max_length=254)
    age = models.IntegerField(null=True)
    phonenumber = models.TextField(max_length=15)
    address = models.TextField(max_length=254)
    Image = models.FileField(upload_to='images/', null=True)
    datetime = models.DateTimeField(auto_now=True, null=True)
    user_status = models.TextField(default='pending', max_length=50, null=True)
    otp = models.IntegerField(null=True)
    otp_status = models.TextField(default='pending', max_length=60, null=True)
    Last_Login_Time = models.TimeField(null=True)
    Last_Login_Date = models.DateField(null=True)  # Removed auto_now_add
    No_Of_Times_Login = models.IntegerField(default=0, null=True)

    class Meta:
        db_table = 'user'

class Contact_Model(models.Model):
    yourname = models.CharField(max_length=50)
    youremail = models.EmailField(max_length=254)
    phone = models.TextField(max_length=15)
    Message = models.TextField(max_length=250,null=True)
    class Meta:
        db_table="contact"

class Dataset_Model(models.Model):
   Data_id = models.AutoField(primary_key=True)
   Image = models.ImageField(upload_to='media/',null=True) 
   class Meta:
        db_table = "upload"

class Predict_Model(models.Model):
    predict_id = models.AutoField(primary_key=True)
    Field_1 = models.CharField(max_length = 60, null = True)
    Field_2 = models.CharField(max_length = 60, null = True)
    Field_3 = models.CharField(max_length = 60, null = True)
    Field_4 = models.CharField(max_length = 60, null = True)
    Field_5 = models.CharField(max_length = 60, null = True)
    Field_6 = models.CharField(max_length = 60, null = True)
    Field_7 = models.CharField(max_length = 60, null = True)
    class Meta:
        db_table = "predict_detail"

class Last_login(models.Model):
    Id = models.AutoField(primary_key = True)
    Login_Time = models.DateTimeField(auto_now = True, null = True)

    class Meta:
        db_table = "last_login"