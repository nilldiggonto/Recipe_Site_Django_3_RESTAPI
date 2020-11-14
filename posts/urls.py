from django.urls import path
from .views import post_list

app_name = 'posts'
urlpatterns = [
    path('post/',post_list,name='post_list'),
]