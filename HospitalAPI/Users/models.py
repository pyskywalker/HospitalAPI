from django.db import models
# Create your models here.
from django.db import models
from datetime import timezone
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_user(self,username,password,**other_fields):
        
        if not username:
            raise ValueError(gettext_lazy("Provide a Password"))
        user=self.model(username=username,**other_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        return self.create_user(username,password,**other_fields)
class HospitalRoom(models.Model):
    room_number=models.CharField(max_length=5)
    description=models.TextField()
    def __str__(self):
        return f"Room {self.room_number}"
class UserType(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.id}:{self.name}'
class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=20,unique=True)
    room=models.OneToOneField(HospitalRoom,on_delete=models.SET_NULL,null=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    usertype=models.ForeignKey(UserType,on_delete=models.SET_NULL,null=True)
    phone=models.CharField(max_length=10,blank=True)
    description=models.TextField(null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.username}"
    is_staff=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)

    objects= CustomAccountManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=[]
