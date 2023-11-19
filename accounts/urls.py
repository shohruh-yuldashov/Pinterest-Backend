from django.urls import path
from .views import UserAPIView, RegisterApiView, DecoratedTokenRefreshView

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('users/', UserAPIView.as_view()),

    # path('token/', TokenObtainPairView.as_view(), name='get-token'),
    path('refresh-token/', DecoratedTokenRefreshView.as_view(), name='refresh-token'),
]
