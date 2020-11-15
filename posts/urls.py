from django.urls import path
from .views import post_list,post_detail,post_create,post_update,post_delete

app_name = 'posts'
urlpatterns = [
    path('create/',post_create,name='post_create'),
    path('post/',post_list,name='post_list'),
    path('<slug:slug>/',post_detail,name='post_detail'),
    path('edit/<slug:slug>/',post_update,name='post_update'),
    path('delete/<slug:slug>/',post_delete,name='post_delete'),
]