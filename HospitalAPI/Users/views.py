from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.response import Response
from .models import User, HospitalRoom
from .serializers import RegisterSerializer, UserSerializer,HospitalRoomsSerializer
#from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from knox.views import LoginView as KnoxLoginView
from knox import views as knox_views
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login

class UsersAPI(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset=User.objects.filter(is_staff=False)
    serializer_class=UserSerializer
    # def create(self, validated_data):
    #     room_data = validated_data.pop('staffs_room')
    #     room = HospitalRoom.objects.create(**validated_data)
    #     for album_data in albums_data:
    #         User.objects.create(artist=musician, **album_data)
    #     return musician
class RoomAPI(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset=HospitalRoom.objects.all()
    serializer_class=HospitalRoomsSerializer
class UserAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        #"token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
