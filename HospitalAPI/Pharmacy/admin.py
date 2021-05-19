from django.contrib import admin
from .models import Medicine,MedicineBrand,MSDZone,Batch,Supplier
# Register your models here.
mymodels=[Medicine,MedicineBrand,MSDZone,Batch,Supplier]
for model in mymodels:
    admin.site.register(model)