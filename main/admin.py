from django.contrib import admin

from main.models import Post, Board, Comment, Like

admin.site.register((Post, Board, Comment, Like))
