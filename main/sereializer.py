from rest_framework import serializers
from main.models import *
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import Documents


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ('name',)
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
        read_only_fields = ('user','slug',)


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'


class SlugSerializer(serializers.Serializer):
    slug = serializers.CharField()


class DocSerializer(DocumentSerializer):

    class Meta:
        document = Documents
        fields = ('name', 'slug')
