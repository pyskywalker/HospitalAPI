from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Patient,Appointment,Labtest,LabTestItem,Diagnoses
from .serializers import PatientSerializer,AppointmentSerializer,LabTestItemSerializer,LabtestSerializer,DiagnosesSerializer
# Create your views here.
class PatientAPI(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer
class AppointmentAPI(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer
class LabtestAPI(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset=Labtest.objects.all()
    serializer_class=LabtestSerializer
class LabItemAPI(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset=LabTestItem.objects.all()
    serializer_class=LabTestItemSerializer
class DiagnosesAPI(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset=Diagnoses.objects.all()
    serializer_class=DiagnosesSerializer
# class MedicineDetailView(generics.RetrieveCreateDestroyAPIView):
#     permission_classes=(IsAuthenticated,)
#     def query_set(id):
#         return pass
#     serializer_class=(IsAuthenticated,)

# class BatchDetailView(generics.RetrieveCreateDestroyAPIView):
#     permission_classes=(IsAuthenticated,)
#     def query_set(id):
#         return pass
#     serializer_class=BatchSerializer