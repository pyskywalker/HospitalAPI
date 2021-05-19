from django.urls import path
from .views import UsersAPI,RoomAPI
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('',UsersAPI.as_view(),name="user_api"),
    path('rooms/',RoomAPI.as_view(),name="hospitalrooms")
]