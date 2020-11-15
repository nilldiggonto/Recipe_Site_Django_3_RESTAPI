from django.db import models
# from posts.models import Post
from django.conf import settings

##Generic Foreign Key
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


#Model Manager
class CommentManager(models.Manager):
    def filter_by_instance(self,instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id

        qs = super(CommentManager,self).filter(content_type = content_type, object_id = obj_id)
        return qs
        # comment = Comment.objects.filter(content_type= content_type, object_id = obj_id)


# Create your models here.
class Comment(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    # post        = models.ForeignKey(Post,on_delete= models.CASCADE,related_name='comment_post')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id') 




    content     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)


    objects = CommentManager()

    def __str__(self):
        return self.user.username