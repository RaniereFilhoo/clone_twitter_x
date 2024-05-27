from django.shortcuts import render, redirect
from .models import Home
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login

def home(request):
    posts = Home.objects.all()
    return render(request, 'clone_x_app/home.html', {'posts': posts})

def logout(request):
    posts = Home.objects.all()
    return render(request, 'clone_x_app/logout.html', {'posts': posts})

def cadastro(request):
    if request.method == "GET":
        return render(request, 'clone_x_app/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse username')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return redirect('login')


def login_view(request):
    if request.method == "GET":
        return render(request, 'clone_x_app/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user is not None:
            login(request, user)

            return redirect('home')
        else:
            return HttpResponse('Email ou senha inválidos')