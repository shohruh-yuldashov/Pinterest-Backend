from django.urls import path

from main.views import TestApiView

urlpatterns = [
    path('test/', TestApiView.as_view(), name='test')
]
