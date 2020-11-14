from django.shortcuts import render

# Create your views here.
def post_home(request):
    template_name = 'posts/list.html'
    return render(request,template_name)