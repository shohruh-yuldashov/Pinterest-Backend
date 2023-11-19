from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import UserDetailSerializer, RegisterInputSerializer, AccountCreatedSerializer, InvalidDataSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class RegisterApiView(APIView):
    serializer_class = RegisterInputSerializer
    parser_classes = (JSONParser,)
    # filter_class = UserDetailSerializer

    # manual_parameters = [
    #     openapi.Parameter(name='first_name', in_=openapi.IN_FORM, type=openapi.TYPE_STRING, description='First Name',
    #                       required=True),
    #     openapi.Parameter(name='last_name', in_=openapi.IN_FORM, type=openapi.TYPE_STRING, description='Last Name'),
    #     openapi.Parameter(name='username', in_=openapi.IN_FORM, type=openapi.TYPE_STRING, description='Username',
    #                       required=True),
    #     openapi.Parameter(name='email', in_=openapi.IN_FORM, type=openapi.TYPE_STRING, description='Email',
    #                       required=True),
    # ]

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


class DecoratedTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: "Test",
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserAPIView(APIView):

    def get(request):
        users = User.objects.all()
        serializer = UserDetailSerializer(users, many=True)
        return Response(serializer.data)
