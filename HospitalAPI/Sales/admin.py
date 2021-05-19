from django.contrib import admin
from .models import Order,OrderType,OrderedItem,Invoice,Transaction,AppointmentFee
# Register your models here.
mymodels=[Order,OrderType,OrderedItem,Invoice,Transaction,AppointmentFee]
for model in mymodels:
    admin.site.register(model)