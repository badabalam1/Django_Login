from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib.sessions.models import Session
# from snippets.serializers import SnippetSerializer

# Create your views here.


@login_required(login_url="/login/")
def main(request):
    return render(request, 'user/index.html', {'name': '메인'})


def index(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # if User.objects.filter(username=request.POST['username']):
            #     form = RegisterForm()
            #     return render(request, 'user/register.html', {'name': '회원가입', 'form': form, 'result': '이미 등록된 username입니다.'})
            # else:
            user = User.objects.create_user(
                username=form.cleaned_data['username'], password=form.cleaned_data['password'], email=form.cleaned_data['email'])
            print("1234")
            if user is not None:
                print("123456")
                login(request, user)
                return redirect('main')
        else:
            form = RegisterForm()
            return render(request, 'user/register.html', {'name': '회원가입', 'form': form, 'result': '이미 등록된 username입니다.'})

    else:
        form = RegisterForm()
        return render(request, 'user/register.html', {'name': '회원가입', 'form': form})


def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(request.POST['username'])
        print(request.POST['password'])
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            form = LoginForm()
            return render(request, 'user/login.html', {'name': '로그인', 'result': '아이디 혹은 비밀번호가 잘못되었습니다.'})
    else:
        form = LoginForm()
        return render(request, 'user/login.html', {'name': '로그인', 'form': form})


def Logout(request):
    logout(request)
    return redirect('login')
