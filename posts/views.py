from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    template_name = 'posts/list.html'
    queryset = Post.objects.all()
    context = {
        'object_list':queryset,

    }
    return render(request,template_name,context)