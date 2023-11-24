from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Board(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=255)
    posts = models.ManyToManyField('Post', related_name='boards')
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    image = models.FileField(upload_to='media/')
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    link = models.URLField(blank=True, null=True)
    hashtag = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    post = models.ForeignKey(Post, models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    post = models.ForeignKey(Post, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Subscriber(models.Model):
    email = models.EmailField()
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
