from django.contrib import admin
from .models import Patient,PatientType,Appointment,Labtest,LabTestItem,Diagnoses
# Register your models here.
mymodels=[Patient,PatientType,Appointment,Labtest,LabTestItem,Diagnoses]
for model in mymodels:
    admin.site.register(model)
