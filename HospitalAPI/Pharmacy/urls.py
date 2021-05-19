from django.urls import path
from .views import MedicineAPI,BatchAPI,SupplierAPI
# urlpatterns=[
#     path('orders',OrderAPI.as_view(),name="orders"),
#     path('items',OrderedItemsAPI.as_view(),name="items"),
#     path('invoice',InvoiceAPI.as_view(),name="ordeinvoicers"),
#     path('Appointment',AppointmentAPI.as_view(),name="appointment"),
#     path('Transaction',TransactionAPI.as_view(),name="transactions"),

# ]
urlpatterns=[
    path('medicine',MedicineAPI.as_view(),name="medicine"),
    path('batches',BatchAPI.as_view(),name="batch"),
    path('suppliers',SupplierAPI.as_view(),name="suppliers"),
]