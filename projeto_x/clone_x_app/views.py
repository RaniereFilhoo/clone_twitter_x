from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Comentario
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView 
from .forms import ComentarioForm
from django.views.generic import ListView

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
        

        return redirect('listaComentarios')


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

class ComentarioUpdate(UpdateView):
    model = Comentario
    fields = ['comentario']
    success_url = reverse_lazy('listaComentarios')

class ComentarioDetail(DetailView):
    queryset = Comentario.objects.all()

class ComentarioDelete(DeleteView):
    queryset = Comentario.objects.all()
    success_url = reverse_lazy('listaComentarios')



