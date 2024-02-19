from django.db import models

class register_tb(models.Model):
    Name=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    Adress=models.CharField(max_length=20)
    Place=models.CharField(max_length=20)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
class image_tb(models.Model):
    file=models.FileField()
class country_tb(models.Model):
    name=models.CharField(max_length=20)
class state_tb(models.Model):
    name=models.CharField(max_length=20)
    Country_id=models.ForeignKey(country_tb,on_delete=models.CASCADE)
