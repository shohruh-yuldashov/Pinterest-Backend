from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers

from .models import User


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


class UpdatePasswordSerializer(Serializer):
    current_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)


class AccountCreatedSerializer(serializers.Serializer):
    detail = serializers.CharField(default='Account successfully created.')


class InvalidDataSerializer(serializers.Serializer):
    detail = serializers.CharField(default="Input data is invalid. Check and try again.")


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


class UnauthorizedSerializer(serializers.Serializer):
    detail = serializers.CharField(default="Authentication credentials were not provided.")


class PasswordUpdatedSerializer(serializers.Serializer):
    detail = serializers.CharField(default="Password updated successfully.")


class OldPasswordInvalidSerializer(serializers.Serializer):
    detail = serializers.CharField(default="Your old password is invalid.")


class PasswordsAreSameSerializer(serializers.Serializer):
    detail = serializers.CharField(default="Your old and new passwords are same.")