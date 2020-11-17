from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField,SerializerMethodField


from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_id',
            'content_object',
            'parent',
            'content'
        ]