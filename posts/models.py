from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True,null=True)
    content     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:post_detail',args= [self.slug])

    def get_update_url(self):
        return reverse('posts:post_update',args= [self.slug])

    class Meta:
        ordering = ['-timestamp','-updated']

