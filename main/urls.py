from django.urls import path

from main.views import *

urlpatterns = [
    path('test/', TestApiView.as_view(), name='test'),
    path('post/', PostView.as_view(), name='create_post'),
    path('post-update/<int:pk>/', PostUpdateView.as_view(), name='edit_post'),
    path('board/', BoardView.as_view(), name='create_board'),
    path('board-update/<int:pk>/', BoardUpdateView.as_view(), name='edit_board'),
    path('comment/', CommentView.as_view(), name='create_comment'),
    path('comment-update/<int:pk>/', CommentUpdateView.as_view(), name='edit_comment'),
    path('like/', LikeViews.as_view(), name='create_like'),
    path('like-update/<int:pk>', LikeUpdateView.as_view(), name='edit_like'),
    path('post/<str:slug>', SlugAPIView.as_view(), name='post_detail'),
]
