from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView


class TestApiView(APIView):

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(name='cart_id', in_=openapi.IN_PATH,
                              type=openapi.TYPE_INTEGER, description='Birnimalar kiritish')
        ])
    def get(self, request):
        return JsonResponse({'message': "test"})