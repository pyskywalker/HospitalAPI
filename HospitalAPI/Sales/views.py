from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.response import Response
from .models import Order,OrderedItem,Invoice,Transaction,Appointment
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer,ItemSerializer,InvoiceSerializer,TransactionSerializer
# Create your views here.
class OrderAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
class OrderedItemAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=OrderedItem.objects.all()
    serializer_class=ItemSerializer
class InvoiceAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer
class AppointmentAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Appointment.objects.all()
    serializer_class=AppointmentSerializer
class TransactionAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Invoice.objects.all()
    serializer_class=TransactionSerializer
