from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.response import Response
from .serializers import RegisterInputSerializer, AccountCreatedSerializer, InvalidDataSerializer, \
    TokenInvalidSerializer, LogInDetailsErrorSerializer, GetTokenSerializer, RefreshTokenSerializer, \
    UpdatePasswordSerializer, UnauthorizedSerializer, PasswordUpdatedSerializer, OldPasswordInvalidSerializer, \
    PasswordsAreSameSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class RegisterApiView(APIView):
    serializer_class = RegisterInputSerializer
    parser_classes = (JSONParser,)

    @swagger_auto_schema(request_body=RegisterInputSerializer, responses={status.HTTP_200_OK: AccountCreatedSerializer, status.HTTP_400_BAD_REQUEST: InvalidDataSerializer}, operation_id='api for account creation', operation_description='Fill the all fields and your account was been created.')
    def post(self, request):
        serializer = RegisterInputSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': "Account successfully created."},
                status=status.HTTP_200_OK
            )

        return Response(
            {'message': "Input data is invalid. Check end try again."},
            status=status.HTTP_400_BAD_REQUEST
        )


class CustomTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: RefreshTokenSerializer,
            status.HTTP_401_UNAUTHORIZED: TokenInvalidSerializer
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenObtainView(TokenObtainPairView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: GetTokenSerializer,
            status.HTTP_401_UNAUTHORIZED: LogInDetailsErrorSerializer
        },
        operation_id='api for token obtain (log in)',
        operation_description='Fill the all fields and you are log in your account.'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UpdatePasswordApiView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdatePasswordSerializer

    @swagger_auto_schema(request_body=UpdatePasswordSerializer, responses={status.HTTP_200_OK: PasswordUpdatedSerializer, status.HTTP_401_UNAUTHORIZED: UnauthorizedSerializer, status.HTTP_400_BAD_REQUEST: OldPasswordInvalidSerializer, status.HTTP_403_FORBIDDEN: PasswordsAreSameSerializer}, operation_id='api for update password', operation_description='Fill the all fields and your password was been updated.')
    def patch(self, request):
        user = request.user
        current_password = request.data.get('current_password')
        if user.check_password(current_password):
            new_password = request.data.get('new_password')
            if current_password == new_password:
                return Response({'detail': "Your old and new passwords are same."})
            else:
                user.set_password(new_password)
                user.save()
                return Response({'detail': 'Password updated successfully.'})
        else:
            return Response({'detail': "Your old password is invalid."})
