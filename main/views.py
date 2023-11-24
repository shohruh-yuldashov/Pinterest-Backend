from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework import generics
from main.sereializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class TestApiView(APIView):

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(name='cart_id', in_=openapi.IN_PATH,
                              type=openapi.TYPE_INTEGER, description='Birnimalar kiritish')
        ])
    def get(self, request):
        return JsonResponse({'message': "test"})


class BoardCreateView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BoardEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]


class PostCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class CommentCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class LikeCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]


class SubscribeAPIView(GenericAPIView):
    serializer_class = EmailSerializer
    permission_classes = ()

    def post(self, request):
        if not Subscriber.objects.filter(email=request.data['email']).exists():
            email_serializer = self.serializer_class(data=request.data)
            email_serializer.is_valid(raise_exception=True)
            email_serializer.save()
        else:
            return Response({'success': False, 'message': 'Already subscribed!'}, status=400)
        return Response({'success': True, 'message': 'Successfully subscribed :)'})
