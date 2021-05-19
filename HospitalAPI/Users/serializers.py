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
        fields="__all__"

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserType
        fields=['id','name','description']
class UserSerializer(serializers.ModelSerializer):
    room_number=serializers.CharField(source="room.room_number",read_only=True)
    usertype_name=serializers.CharField(source="usertype.name",read_only=True)
    usertype_description=serializers.CharField(source="usertype.description",read_only=True)
    class Meta:
        model=User
        fields="__all__"
class RestrictedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','first_name','last_name','room','usertype','phone']