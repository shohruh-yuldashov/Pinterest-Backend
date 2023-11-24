from django.urls import path

from main.views import *

urlpatterns = [
    path('test/', TestApiView.as_view(), name='test'),
    path('post/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/', PostEditView.as_view(), name='edit_post'),
    path('board/', BoardCreateView.as_view(), name='create_board'),
    path('board/<int:pk>/', BoardEditView.as_view(), name='edit_board'),
    path('comment/', CommentCreateView.as_view(), name='create_comment'),
    path('comment/<int:pk>/', CommentEditView.as_view(), name='edit_comment'),
    path('like/', LikeCreateView.as_view(), name='create_like'),
    path('like/<int:pk>', LikeEditView.as_view(), name='edit_like'),
    path('subscribe/', SubscribeAPIView.as_view(), name='subscribe')
]
