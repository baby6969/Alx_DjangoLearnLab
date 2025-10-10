from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


user = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = user
        fields = ['id','username', 'email', 'bio', 'profile_picture']
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
class mata:
    model =user
    fields = ['username', 'email', 'password', 'bio', 'profile_picture']
    
def create(self, validated_date):
    password = validated_data.pop(password)
    user= user (**validated_data)
    user.set_password(password)
    user.save()
    Token.objects.create(user=user)
    return user

class LoginSerializer(serializers.Serializer):
 username = serializers.CharField()
 password = serializers.CharField(write_only=True)
