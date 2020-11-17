from rest_framework import serializers

from posts.models import Post

#create
class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish',
        ]

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # 'id',
            'user',
            'title',
            'slug',
            'content',
            'publish',

        ]


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish',
        ]