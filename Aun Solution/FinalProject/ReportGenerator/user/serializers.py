from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login
from rest_framework.request import Request
from django.core.exceptions import ValidationError



class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2','role']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data:dict[str,str]):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data

    def create(self, data:dict[str,str]) -> User:
        user = User.objects.create_user(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        role = data['role']
        )
        return user
    





class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(max_length=255, read_only=True)
    refresh = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data:dict[str,str]) ->dict[str,str]:
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError('A user with this email and password is not found.')
        else:
            refresh = RefreshToken.for_user(user)
            update_last_login(None, user) 
        return {
            'email':user.email,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }








class UserUpdateSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(write_only=True, required=False)
    new_password = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(required=False) 

    class Meta:
        model = User
        fields = ['username', 'current_password', 'new_password']
    
    def validate(self, data):
        new_password = data.get('new_password')
        current_password = data.get('current_password')
        
        if new_password and not current_password:
            raise ValidationError({"current_password": "Required for password change"})
        
        return data
    
    def update(self, instance, validated_data):
        current_password = validated_data.pop('current_password', None)
        new_password = validated_data.pop('new_password', None)
        
        if new_password:
            if not instance.check_password(current_password):
                raise ValidationError({"current_password": "Incorrect password"})
            instance.set_password(new_password)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
        



 






