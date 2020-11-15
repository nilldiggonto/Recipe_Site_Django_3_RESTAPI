from django.db import models
from posts.models import Post
from django.conf import settings
# Create your models here.
class Comment(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    post        = models.ForeignKey(Post,on_delete= models.CASCADE,related_name='comment_post')
    content     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username