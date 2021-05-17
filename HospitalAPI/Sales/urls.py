from django.urls import path
from .views import OrderAPI,OrderedItemAPI,InvoiceAPI,TransactionAPI
urlpatterns=[
    path('orders',OrderAPI.as_view(),name="orders"),
    path('items',OrderedItemAPI.as_view(),name="items"),
    path('invoice',InvoiceAPI.as_view(),name="ordeinvoicers"),
    #path('Appointment',AppointmentAPI.as_view(),name="appointment"),
    path('Transaction',TransactionAPI.as_view(),name="transactions"),
]