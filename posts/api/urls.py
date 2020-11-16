from django.urls import path
from django.contrib import admin

from .views import PostListAPIView

app_name = 'post_api'
urlpatterns = [
    path('',PostListAPIView.as_view(),name='list_api')
]