from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import UserForm, LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/login/")
def main(request):
    return render(request, 'user/index.html', {'name': '메인'})


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
        return render(request, 'user/register.html', {'name': '회원가입', 'form': form})


def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'user/login.html', {'name': '로그인'})
    else:
        form = LoginForm()
        return render(request, 'user/login.html', {'name': '로그인', 'form': form})


def Logout(request):
    logout(request)
    return redirect('login')
