from comments.models import Comment
from posts.api.permissions import IsOwnerOrReadOnly
from posts.api.paginations import PageNumberPagination,PostLimitOffsetPagination

from rest_framework.generics import ListAPIView
from .serializers import CommentSerializer
from django.db.models import Q

class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self,*args,**kwargs):
        queryset_list = Comment.objects.all()
    #     query = self.request.get('q')
