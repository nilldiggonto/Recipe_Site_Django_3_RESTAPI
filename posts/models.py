from django.db import models
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType

## MODEL MANAGER
class PostManager(models.Manager):
    def active(self,*args,**kwargs):
        return super(PostManager,self).filter(draft=False).filter(publish__lte= timezone.now())


# Create your models here.
class Post(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete= models.CASCADE)
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True,null=True)
    images      = models.ImageField(upload_to='recipe/%y/%m/%d',blank=True,null=True)
    content     = models.TextField()
    draft       = models.BooleanField(default=False)
    publish     = models.DateField(auto_now=False,auto_now_add=False)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:post_detail',args= [self.slug])

    def get_update_url(self):
        return reverse('posts:post_update',args= [self.slug])

    class Meta:
        ordering = ['-timestamp','-updated']

    #For comments
    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_post_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type



def create_slug(instance,new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s"%(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug


##Signal
def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    

pre_save.connect(pre_save_post_receiver,sender=Post)

