from rest_framework.generics import (ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,
                                        CreateAPIView,RetrieveUpdateAPIView)
from .serializers import PostListSerializer,PostDetailSerializer,PostCreateUpdateSerializer
from posts.models import Post

from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q

from rest_framework.filters import SearchFilter,OrderingFilter

from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from .paginations import PostLimitOffsetPagination,PostPageNumberPagination
#create
class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)



#list
class PostListAPIView(ListAPIView):

    # queryset = Post.objects.all()
    serializer_class = PostListSerializer

    #build-in filter
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title','content']

    #build-in pagination
    pagination_class = PostPageNumberPagination

    def get_queryset(self,*args,**kwargs):
        # queryset_list = super(PostListAPIView).get_queryset(*args,**kwargs)
        queryset_list = Post.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains = query) |
                Q(content__icontains = query)
            ).distinct()
        return queryset_list

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
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
