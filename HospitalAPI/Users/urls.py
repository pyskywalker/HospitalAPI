from django.urls import path
from .views import UsersAPI
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('api/',UsersAPI.as_view(),name="user_api"),
]