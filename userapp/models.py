from django.db import models
from mainapp.models import *

# Create your models here.
class feedback(models.Model):
    feed_id = models.AutoField(primary_key=True)
    rating=models.CharField(max_length=100,null=True)
    review=models.CharField(max_length=225,null=True)
    sentiment=models.CharField(max_length=100,null=True)
    reviewer=models.ForeignKey(User_Model, on_delete=models.CASCADE,null=True)
    datetime=models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'feedback_details'
        
class Data_set(models.Model):
   Data_id = models.AutoField(primary_key=True)
   Image = models.ImageField(upload_to='media/') 
   class Meta:
        db_table = "upload_user"