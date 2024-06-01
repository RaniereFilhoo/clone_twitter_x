from django.urls import path
from .views import home, logout
from . import views
from .views import ComentarioCreateView, ComentarioList

urlpatterns = [
    path('', home, name='home'),
    path('logout', logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login', views.login_view, name='login'),
    path('login/', views.logincopy_view, name='logincopy'),
    path('Create/', ComentarioCreateView.as_view(), name='criarComentario'),
    path('home', ComentarioList.as_view(), name='listaComentarios'),
]

