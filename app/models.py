from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Laptops(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    LaptopName=models.CharField(max_length=100)
    LaptopModel=models.CharField(max_length=100)
    Lapimage=models.ImageField()
    Price=models.IntegerField()
    RAM=models.CharField(max_length=100)
    Description=models.TextField()


    def __str__(self):
        return self.LaptopName
        
