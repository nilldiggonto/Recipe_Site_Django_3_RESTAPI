
from django.contrib import admin
from django.urls import path,include
from .views import home_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page,name='home'),
    path('posts/',include('posts.urls',namespace='posts')),
]
