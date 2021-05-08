from rest_framework import serializers
from .models import User,HospitalRoom,UserType
from knox.models import AuthToken

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','username','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['password'])
        return user
class HospitalRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model=HospitalRoom
        fields='_all_'

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserType
        fields='_all_'
class UserSerializer(serializers.ModelSerializer):
    room=HospitalRoomsSerializer()
    usertype=UserTypeSerializer()
    class Meta:
        model=User
        fields='_all_'