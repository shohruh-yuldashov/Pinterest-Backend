from django.urls import path
from .views import RegisterApiView, CustomTokenRefreshView, CustomTokenObtainView, UpdatePasswordApiView

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('token/', CustomTokenObtainView.as_view(), name='get-token'),
    path('refresh-token/', CustomTokenRefreshView.as_view(), name='refresh-token'),
    path('update-password/', UpdatePasswordApiView.as_view(), name='update-password')
]
