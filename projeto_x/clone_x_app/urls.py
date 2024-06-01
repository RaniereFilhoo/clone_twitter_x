from django.urls import path
from .views import home, logout, perfil
from . import views
from .views import ComentarioCreateView

urlpatterns = [
    path('', home, name='home'),
    path('logout', logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login', views.login_view, name='login'),
    path('login/', views.logincopy_view, name='logincopy'),
    path('home', ComentarioCreateView.as_view(), name='criarComentario'),
    path('perfil/', perfil, name='perfil'),
    
]
