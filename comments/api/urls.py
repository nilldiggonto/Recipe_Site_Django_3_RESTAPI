from django.urls import path
from .views import CommentListAPIView

app_name = 'comment_api'
urlpatterns = [
    path('',CommentListAPIView.as_view(),name='list_api'),
]