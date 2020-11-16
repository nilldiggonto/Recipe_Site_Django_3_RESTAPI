from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,get_user_model,login,logout
from .forms import UserLoginForm,UserRegisterForm
# Create your views here.
def login_view(request):
    form = UserLoginForm(request.POST or None)
    title = 'Login'
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request,user)
        return redirect('home')

    context = {
        'form':form,
        'title':title,
    }
    template_name = 'accounts/login.html' 
    return render(request,template_name,context)


def register_view(request):
    title = 'Register'
    form = UserRegisterForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        nuser = authenticate(username = user.username, password = password)
        login(request,nuser)
        return redirect('home')

    template_name = 'accounts/login.html'
    context = {
        'form':form,
        'title':title
    }
    return render(request,template_name,context)


def logout_view(request):
    logout(request)
    # form = UserLoginForm(request.POST or None)
    template_name = 'home.html' 
    return render(request,template_name)