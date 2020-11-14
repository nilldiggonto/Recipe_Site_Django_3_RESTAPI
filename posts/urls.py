from django.urls import path
from .views import post_home

app_name = 'posts'
urlpatterns = [
    path('post/',post_home,name='post_home'),
]