from rest_framework.generics import (ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,
                                        CreateAPIView,RetrieveUpdateAPIView)
from .serializers import PostListSerializer,PostDetailSerializer,PostCreateUpdateSerializer
from posts.models import Post

from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
#create
class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)



#list
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

#detail
class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

#update
class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)

#delete
class PostDestroyAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'