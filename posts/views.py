from django.shortcuts import render,get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.
def post_list(request):
    template_name = 'posts/list.html'
    queryset = Post.objects.all()
    context = {
        'object_list':queryset,

    }
    return render(request,template_name,context)


def post_detail(request,slug):
    instance = get_object_or_404(Post,slug=slug)
    template_name = 'posts/detail.html'
    context = {
        'object':instance
    }
    return render(request,template_name,context)


def post_create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    template_name = 'posts/create.html'
    context = {
        'form':form
    }
    return render(request,template_name,context)
