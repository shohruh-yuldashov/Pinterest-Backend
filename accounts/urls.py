from django.urls import path
from .views import RegisterApiView, CustomTokenRefreshView, CustomTokenObtainView

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('token/', CustomTokenObtainView.as_view(), name='get-token'),
    path('refresh-token/', CustomTokenRefreshView.as_view(), name='refresh-token'),
]
