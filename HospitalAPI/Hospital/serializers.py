from rest_framework import serializers
from .models import PatientType,Patient,Appointment,Labtest,LabTestItem,Diagnoses
from Users.serializers import RestrictedUserSerializer
# from Pharmacy.serializers import MedicineBrandSerializer
from rest_framework import serializers

class PatientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=PatientType
        fields=['id','name','description']
class PatientSerializer(serializers.ModelSerializer):
    patient_type=PatientTypeSerializer()
    class Meta:
        model=Patient
        fields='__all__'
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields='__all__'
class LabtestSerializer(serializers.ModelSerializer):
    appointment=AppointmentSerializer()
    technician=RestrictedUserSerializer()
    class Meta:
        model=Labtest
        fields='__all__'
class LabTestItemSerializer(serializers.ModelSerializer):
    test=LabtestSerializer()
    class Meta:
        model=LabTestItem
        fields='__all__'
class DiagnosesSerializer(serializers.ModelSerializer):
    class Meta:
        appointment=AppointmentSerializer()
        model=Diagnoses
        fields='__all__'