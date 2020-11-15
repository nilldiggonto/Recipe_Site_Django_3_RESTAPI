from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
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
    info ='Create'
    form = PostForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,'Successfully Created')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,'Something went Wrong')

    template_name = 'posts/create.html'
    context = {
        'form':form,
        'info':info,
    }
    return render(request,template_name,context)


def post_update(request,slug):
    info= 'Edit'
    instance = get_object_or_404(Post,slug=slug)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,'Successfully Updated')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,'Something went wrong ')

    template_name = 'posts/create.html'
    context = {
        'object':instance,
        'form':form,
        'info':info,
    }
    return render(request,template_name,context)



def post_delete(request,slug):
    instance = get_object_or_404(Post,slug=slug)
    instance.delete()
    messages.success(request,'Post Successfully Deleted')
    return redirect('posts:post_list')

