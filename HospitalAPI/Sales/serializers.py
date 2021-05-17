from rest_framework import serializers
from .models import Order, OrderedItem,Invoice,OrderType,Invoice,Transaction,AppointmentFee
from Pharmacy.serializers import MedicineSerializer,SupplierSerializer
from Hospital.serializers import PatientSerializer

class OrderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderType()
        fields="__all__"
class OrderSerializer(serializers.ModelSerializer):
    order_type=OrderTypeSerializer()
    supplier=SupplierSerializer
    class Meta:
        model=Order
        fields="__all__"
    
class ItemSerializer(serializers.ModelSerializer):
    customer_order=OrderSerializer()
    medicine=MedicineSerializer()
    class Meta:
        model=OrderedItem
        fields="__all__"

class InvoiceSerializer(serializers.ModelSerializer):
    order=OrderSerializer()
    class Meta:
        model=Invoice
        fields="__all__"

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields="__all__"
class AppointmentFeeSerializer(serializers.ModelSerializer):
    patient=PatientSerializer()
    transaction=TransactionSerializer()
    class Meta:
        model=AppointmentFee
        fields="__all__"