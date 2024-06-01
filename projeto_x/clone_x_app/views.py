from django.shortcuts import render, redirect
from .models import Comentario
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView 
from .forms import ComentarioForm
from django.http import JsonResponse

def home(request):
    posts = Comentario.objects.all()
    return render(request, 'clone_x_app/home.html', {'posts': posts})

def logout(request):
    posts = Comentario.objects.all()
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
        user = authenticate(username=username, password=senha)
        login(request, user)
        

        return redirect('home')


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
        
def logincopy_view(request):
    if request.method == "GET":
        return render(request, 'clone_x_app/logincopy.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user is not None:
            login(request, user)

            return redirect('home')
        else:
            return HttpResponse('Email ou senha inválidos')

def perfil(request):
    user = request.user
    return render(request, 'clone_x_app/perfil.html', {'user': user})


        
class ComentarioCreateView(CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'clone_x_app/home.html'
    success_url = 'home'

    def form_valid(self, form):
        comentario = form.save()
        return JsonResponse({
            'comentario': comentario.comentario,
        })
