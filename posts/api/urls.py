from django.urls import path
from django.contrib import admin

from .views import PostListAPIView,PostDetailAPIView,PostUpdateAPIView,PostDestroyAPIView,PostCreateAPIView

app_name = 'post_api'
urlpatterns = [
    path('',PostListAPIView.as_view(),name='list_api'),
    path('create/',PostCreateAPIView.as_view(),name='create_api'),
    path('<slug:slug>/',PostDetailAPIView.as_view(),name='detail_api'),
    path('update/<slug:slug>/',PostUpdateAPIView.as_view(),name='update_api'),
    path('delete/<slug:slug>/',PostDestroyAPIView.as_view(),name='delete_api'),
]