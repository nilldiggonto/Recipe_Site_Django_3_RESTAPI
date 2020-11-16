from rest_framework.generics import ListAPIView
from .serializers import PostSerializer
from posts.models import Post

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer