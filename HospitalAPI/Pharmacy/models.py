from django.db import models

# Create your models here.
from django.db import models
from django.db import models
from Users.models import User
from django.utils import timezone
from Users.models import User

# Create your models here.
class MSDZone(models.Model):
    zone_name=models.CharField(max_length=50)
    zone_location=models.CharField(max_length=30)
    description=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.zone_name}'
    

class MedicineBrand(models.Model):
    brand_name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    description=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.brand_name}'
    

class Batch(models.Model):
    batch_number=models.IntegerField()
    medicine_brand=models.ForeignKey(MedicineBrand,on_delete=models.PROTECT)
    medicine_name=models.CharField(max_length=30)
    description=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.id}'
   

class Medicine(models.Model):
    serialnumber=models.IntegerField()
    unit_of_measure = models.CharField(max_length=2)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    status=models.TextField()
    price=models.FloatField()
    batch=models.ForeignKey(Batch, on_delete=models.CASCADE)
    msd_zone=models.ForeignKey(MSDZone, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.id}'
   

class Supplier(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    contacts=models.CharField(max_length=15)
    def __str__(self):
        return f'{self.name}'







    