from rest_framework import serializers
from main.models import *

from .documents import Document
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer


class BoardSerializer(serializers.ModelSerializer):
    # boards = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())

    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ('user',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    like = LikeSerializer(many=True, read_only=True)
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user',)


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'


class SlugSerializer(serializers.Serializer):
    slug = serializers.CharField()


class PostDocumentSerializer(DocumentSerializer):
    price = serializers.FloatField()

    class Meta:
        document = Document
        fields = ('name', 'slug' 'description')


