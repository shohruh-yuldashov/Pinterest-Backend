from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     """Customizes JWT default Serializer to add more information about user"""
#     @classmethod
#     def get_token(cls, user):
#         print('test')
#         token = super().get_token(user)
#         token['email'] = user.email
#         token['is_superuser'] = user.is_superuser
#         token['is_staff'] = user.is_staff
#
#         print(token)
#
#         return token
#
#
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'token')

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    # def get_token(self, user):
    #     refresh = RefreshToken.for_user(user)
    #     return {
    #         'refresh': str(refresh),
    #         'access': str(refresh.access_token),
    #     }


class UserDetailSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class RegisterInputSerializer(Serializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    def create(self, validated_data):
        instance = self.Meta.model(is_active=True, **validated_data)
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


class AccountCreatedSerializer(serializers.Serializer):
    message = serializers.CharField(default='Account successfully created.')


class InvalidDataSerializer(serializers.Serializer):
    message = serializers.CharField(default="Input data is invalid. Check end try again.")


class TokenInvalidSerializer(serializers.Serializer):
    detail = serializers.CharField(default="Token is invalid or expired.")
    code = serializers.CharField(default="token_not_valid.")


class LogInDetailsErrorSerializer(serializers.Serializer):
    detail = serializers.CharField(default="No active account found with the given credentials.")


class GetTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField(default="refresh token")
    access = serializers.CharField(default="access token.")


class RefreshTokenSerializer(serializers.Serializer):
    access = serializers.CharField(default="access token.")


# class CustomRegisterSerializer(RegisterSerializer):
#
#     name = serializers.CharField(max_length=50)
#     username = serializers.CharField(max_length=50)
#
#     def get_cleaned_data(self):
#         super(CustomRegisterSerializer, self).get_cleaned_data()
#
#         return {
#             'password': self.validated_data.get('password', ''),
#             'name': self.validated_data.get('name', ''),
#             'username': self.validated_data.get('username', '')
#         }