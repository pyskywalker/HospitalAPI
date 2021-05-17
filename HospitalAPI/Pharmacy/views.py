from django.shortcuts import render
from .models Batch,Medicine,Supplier
from .serializers import BatchSerializer,MedicineSerializer,SupplierSerializer
# Create your views here.
class MedicineAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Medicine.objects.all()
    serializer_class=MedicineSerializer
class BatchAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Batch.objects.all()
    serializer_class=BatchSerializer
class SupplierAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=Supplier.objects.all()
    serializer_class=SupplierSerializer

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


