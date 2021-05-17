from django.urls import path
from .views import PatientAPI,AppointmentAPI,LabtestAPI,LabItemAPI,DiagnosesAPI
urlpatterns=[
    path('patients',PatientAPI.as_view(),name="patients"),
    path('appointments',AppointmentAPI.as_view(),name="appointment"),
    path('labtests',LabtestAPI.as_view(),name="labtests"),
    path('labitems',LabItemAPI.as_view(),name="labitems")
]