from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from os.path import splitext

User = get_user_model()


def slugify_upload(instance, filename):
    folder = instance._meta.model_name
    name, ext = splitext(filename)
    name_t = slugify(name) or name
    return f"{folder}/{name_t}{ext}"


class Board(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    image = models.FileField(upload_to=slugify_upload, null=True, blank=True)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    link = models.URLField(blank=True, null=True)
    hashtag = models.CharField(max_length=100)
    board = models.ForeignKey(Board, models.CASCADE)
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

