from django.urls import path
from django.contrib import admin
from .views import UserCreateAPIView,UserLoginAPIView

app_name = 'accounts_api'
urlpatterns = [
    path('register/',UserCreateAPIView.as_view(),name='user_create'),
    path('login/',UserLoginAPIView.as_view(),name='user_login'),

]