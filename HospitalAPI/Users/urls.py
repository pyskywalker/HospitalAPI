from django.urls import path
from .views import UserAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('api/',UserAPIView.as_view(),name="user_api"),
]