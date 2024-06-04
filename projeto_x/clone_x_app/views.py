from django.shortcuts import render, redirect
from .models import Comentario
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView 
from .forms import ComentarioForm
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import PerfilForm


def home(request):
    posts = Comentario.objects.all()
    return render(request, 'clone_x_app/home.html', {'posts': posts})

def logout(request):
    posts = Comentario.objects.all()
    return render(request, 'clone_x_app/logout.html', {'posts': posts})

def cadastro(request):
    if request.method == "POST":
       
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

        
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            
            perfil = form.save(commit=False)
            perfil.user = request.user 
            perfil.save()

       
        return redirect('listaComentarios')

    else:
        
        form = PerfilForm()
        return render(request, 'clone_x_app/cadastro.html', {'form': form})

def login_view(request):
    if request.method == "GET":
        return render(request, 'clone_x_app/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user is not None:
            login(request, user)

            return redirect('listaComentarios')
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

            return redirect('listaComentarios')
        else:
            return HttpResponse('Email ou senha inválidos')
        
class ComentarioCreateView(CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'clone_x_app/home.html'
    success_url = 'home'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.autor = self.request.user
        self.object.save()
        return super().form_valid(form)
    
class ComentarioList(ListView):
    model = Comentario
    template_name = 'clone_x_app/home.html'
    context_object_name = 'comentarios'
    ordering = ['-data_criacao']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        return context


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Comentario, Perfil
from .forms import ComentarioForm, PerfilForm

@login_required
def profile(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user, defaults={'nome': request.user.username})
    return render(request, 'clone_x_app/perfil.html', {'perfil': perfil})

@login_required
def update_profile(request):
    user_profile = Perfil.objects.get(user=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PerfilForm(instance=user_profile)

    return render(request, 'update_profile.html', {'form': form, 'user_profile': user_profile})
