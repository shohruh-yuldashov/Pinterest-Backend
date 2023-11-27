from xml.dom.minidom import Document

from django.db.models import Q
from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from main.sereializer import *
from rest_framework.permissions import IsAuthenticated
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    SearchFilterBackend,
    SuggesterFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination

from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION

class TestApiView(APIView):

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(name='cart_id', in_=openapi.IN_PATH,
                              type=openapi.TYPE_INTEGER, description='Birnimalar kiritish')
        ])
    def get(self, request):
        return JsonResponse({'message': "test"})


class BoardView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BoardSerializer

    def get(self, request):
        board = Board.objects.filter(user_id=request.user.id)
        board_serializer = BoardSerializer(board, many=True)
        return Response(board_serializer.data)

    @swagger_auto_schema(request_body=BoardSerializer)
    def post(self, request):
        name = request.data.get('name')
        board = Board.objects.create(
            user_id=request.user.id,
            name=name
        )
        board.save()
        board_serializer = BoardSerializer(board)
        return Response(board_serializer.data)


class BoardUpdateView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BoardSerializer

    def get(self, request, pk):
        board = Board.objects.filter(Q(user_id=request.user.id) & Q(pk=pk))
        board_serializer = BoardSerializer(board)
        return Response(board_serializer.data)

    def patch(self, request, pk):
        name = request.data.get('name', None)
        board = Board.objects.get(Q(user_id=request.user.id) & Q(pk=pk))
        if name:
            board.name = name
        board.save()
        board_serializer = BoardSerializer(board)
        return Response(board_serializer.data)

    def delete(self, request, pk):
        Board.objects.get(Q(pk=pk) & Q(user_id=request.user.id)).delete()
        return Response(status=204)


class PostView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get(self, request):
        post = Post.objects.filter(user_id=request.user)
        p_serializer = PostSerializer(post, many=True)
        return Response(p_serializer.data)

    def post(self, request):
        user = request.user.id
        name = request.data.get('name')
        description = request.data.get('description')
        link = request.data.get('link')
        hashtag = request.data.get('hashtag')
        board = request.data.get('board')
        image = request.FILES.getlist('image')

        post = Post.objects.create(
            user_id=user,
            slug=slugify(name),
            image=image,
            name=name,
            description=description,
            link=link,
            hashtag=hashtag,
            board_id=board
        )
        post.save()

        po_ser = PostSerializer(post)
        return Response(po_ser.data)


class PostUpdateView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = PostSerializer

    def patch(self, request, pk):
        image = request.FILES.getlist('image', None)
        name = request.data.get('name', None)
        des = request.data.get('description', None)
        link = request.data.get('link', None)
        hash = request.data.get('hashtag', None)

        post = Post.objects.get(Q(user_id=request.user.id) & Q(pk=pk))
        if image:
            post.image = image
        if name:
            post.name = name
        if des:
            post.description = des
        if link:
            post.link = link
        if hash:
            post.hashtag = hash
        post.save()

        po_ser = PostSerializer(post)
        return Response(po_ser.data)

    def delete(self, request, pk):
        Post.objects.get(Q(pk=pk) & Q(user_id=request.user.id)).delete()
        return Response(status=204)


class CommentView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def get(self, request):
        comment = Comment.objects.filter(user_id=request.user.id)
        c_seria = CommentSerializer(comment, many=True)
        return Response(c_seria.data)

    def post(self, request):
        comment = request.POST.get('comment')
        pp = request.POST.get('post')

        cc = Comment.objects.create(
            post_id=pp,
            text=comment,
            user_id=request.user.id
        )
        cc.save()
        coment_serializer = CommentSerializer(cc)
        return Response(coment_serializer.data)


class CommentUpdateView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def patch(self, request, pk):
        text = request.POST.get('comment')

        com = Comment.objects.get(Q(user_id=request.user.id) & Q(pk=pk))
        if text:
            com.text = text
        com.save()
        comment_serializer = CommentSerializer(com)
        return Response(comment_serializer.data)

    def delete(self, request, pk):
        Comment.objects.get(Q(user_id=request.user.id) & Q(pk=pk)).delete()
        return Response(status=204)


class LikeViews(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeSerializer

    def get(self, request):
        like = Like.objects.filter(user_id=request.user.id)
        lik_ser = LikeSerializer(like, many=True)
        return Response(lik_ser.data)

    def post(self, request):
        post = request.POST.get('post')
        like = Like.objects.create(
            post_id=post,
            user_id=request.user.id
        )
        like.save()
        like_serializer = LikeSerializer(like)
        return Response(like_serializer.data)


class LikeUpdateView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeSerializer

    def delete(self, request, pk):
        Like.objects.get(Q(user_id=request.user.id) & Q(pk=pk)).delete()
        return Response(status=204)


class SubscribeAPIView(GenericAPIView):
    serializer_class = EmailSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        if not Subscriber.objects.filter(email=request.data['email']).exists():
            email_serializer = self.serializer_class(data=request.data)
            email_serializer.is_valid(raise_exception=True)
            email_serializer.save()
        else:
            return Response({'success': False, 'message': 'Already subscribed!'}, status=400)
        return Response({'success': True, 'message': 'Successfully subscribed :)'})


class UnsubscribeAPIView(GenericAPIView):
    serializer_class = EmailSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        email_serializer = self.serializer_class(data=request.data)
        email_serializer.is_valid(raise_exception=True)

        email = email_serializer.validated_data['email']

        try:
            subscriber = Subscriber.objects.get(email=email)
            subscriber.delete()
            return Response({'success': True, 'message': 'Successfully unsubscribed :)'})
        except Subscriber.DoesNotExist:
            return Response({'success': False, 'message': 'Email not found. Unable to unsubscribe :('}, status=404)


class SlugAPIView(RetrieveAPIView):
    permission_classes = ()
    serializer_class = PostSerializer

    @swagger_auto_schema(query_serializer=SlugSerializer)
    def get(self, request):
        slug = self.request.query_params.get('slug', None)
        if slug is not None:
            todo = Post.objects.filter(slug=slug).first()
        else:
            todo = Post.objects.first()
        pntress_serializer = self.get_serializer(todo)
        return Response(pntress_serializer.data)


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class SearchViewSet(DocumentViewSet):
    document = Document
    serializer_class = PostDocumentSerializer
    pagination_class = CustomPageNumberPagination

    filter_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend,
    ]

    search_fields = (
        'name',
        'slug',
        'description',

    )

    filter_fields = {
        'name': 'name',
        'slug': 'slug',
        'description': 'description',
    }

    suggester_fields = {
        'name': {
            'field': 'name.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
    }

    def list(self, request, *args, **kwargs):
        search_term = self.request.query_params.get('search', '')
        query = Q('multi_match', query=search_term, fields=self.search_fields)
        queryset = self.filter_queryset(self.get_queryset().query(query))
        print('Queryset >>>>>', queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
