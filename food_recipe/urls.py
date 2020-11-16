from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .views import home_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page,name='home'),
    path('account/',include('accounts.urls',namespace='accounts')),
    path('posts/',include('posts.urls',namespace='posts')),
    path('post/api/',include('posts.api.urls',namespace='post_api')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
