from django.urls import path
from .views import post_list,post_detail

app_name = 'posts'
urlpatterns = [
    path('post/',post_list,name='post_list'),
    path('post/<slug:slug>/',post_detail,name='post_detail'),
]