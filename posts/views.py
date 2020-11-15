from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect,Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.utils import timezone

from django.core.paginator import Page,PageNotAnInteger,Paginator,EmptyPage
# Create your views here.
def post_list(request):
    template_name = 'posts/list.html'
    today = timezone.now().date()
    #queryset_list = Post.objects.filter(draft=False).filter(publish__lte = timezone.now())
    queryset_list = Post.objects.active()#.order_by('-timestamp')
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list,2)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list':queryset,
        'today':today,

    }
    return render(request,template_name,context)


def post_detail(request,slug):
    today = timezone.now().date()
    instance = get_object_or_404(Post,slug=slug)
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    template_name = 'posts/detail.html'
    context = {
        'object':instance,
        'today':today,
    }
    return render(request,template_name,context)


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    info ='Create'
    form = PostForm(request.POST, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
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
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    info= 'Edit'
    instance = get_object_or_404(Post,slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
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
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,slug=slug)
    instance.delete()
    messages.success(request,'Post Successfully Deleted')
    return redirect('posts:post_list')

