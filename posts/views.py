from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect,Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Page,PageNotAnInteger,Paginator,EmptyPage
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
from comments.forms import CommentForm 
from django.contrib.auth.decorators import login_required
# Create your views here.
def post_list(request):
    template_name = 'posts/list.html'
    today = timezone.now().date()
    #queryset_list = Post.objects.filter(draft=False).filter(publish__lte = timezone.now())
    queryset_list = Post.objects.active()#.order_by('-timestamp')
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()



    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(Q(title__icontains= query)| Q(content__icontains=query)).distinct()
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
        'query':query,

    }
    return render(request,template_name,context)


def post_detail(request,slug):
    today = timezone.now().date()
    instance = get_object_or_404(Post,slug=slug)
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404

    #comment
    # content_type = ContentType.objects.get_for_model(Post)
    # obj_id = instance.id
    # comment = Comment.objects.filter(content_type = content_type, object_id= obj_id)
    # comment = Comment.objects.filter_by_instance(instance)

    ##Comment Form
    initial_data = {
        'content_type': instance.get_post_content_type,
        'object_id': instance.id
    }
    comment_form = CommentForm(request.POST or None, initial=initial_data)
    print(instance.id)
    # print(comment_form)
    if comment_form.is_valid():
        c_type = comment_form.cleaned_data.get('content_type')
        
        content_type = ContentType.objects.get(app_label= 'posts',model='post')
        # print(content_type)
        obj_id = comment_form.cleaned_data.get('object_id')
        content_data = comment_form.cleaned_data.get('content')
        parent_obj = None
        try:
            parent_id   = request.POST.get('parent_id')
        except:
            parent_id = None
        if parent_id:
            parent_qs = Comment.objects.filter(id = parent_id)
            if parent_qs.exists() and parent_qs.count()==1:
                parent_obj = parent_qs.first()
        new_comment,created = Comment.objects.get_or_create(
                                user = request.user,
                                content_type = content_type,
                                object_id = obj_id,
                                content = content_data,
                                parent = parent_obj,)
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
        # print(new_comment)
        # if created:
        #     print('created')
        # else:
        #     print('something wrong')

    comment = instance.comments
    template_name = 'posts/detail.html'
    context = {
        'object':instance,
        'today':today,
        'comments':comment,
        'comment_form':comment_form,
    }
    return render(request,template_name,context)

@login_required(login_url='accounts:login_view')
def post_create(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
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

@login_required(login_url='accounts:login_view')
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


@login_required
def post_delete(request,slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,slug=slug)
    instance.delete()
    messages.success(request,'Post Successfully Deleted')
    return redirect('posts:post_list')

