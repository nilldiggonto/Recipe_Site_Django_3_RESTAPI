from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,Hyperlink,HyperlinkedIdentityField,SerializerMethodField
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
    url = HyperlinkedIdentityField(
        view_name='post_api:detail_api',
        lookup_field='slug'
    )
    delete_url = HyperlinkedIdentityField(
        view_name='post_api:delete_api',
        lookup_field='slug'
    )
    user = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            # 'id',
            'url',
            
            'user',
            'title',
            # 'slug',
            'content',
            'publish',
            'delete_url',

        ]
    def get_user(self,obj):
        return str(obj.user.username)


class PostDetailSerializer(serializers.ModelSerializer):
    user = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'user',
            'title',
            'slug',
            'content',
            'publish',
            'image',
        ]
    def get_user(self,obj):
        return str(obj.user.username)

    def get_image(self,obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image