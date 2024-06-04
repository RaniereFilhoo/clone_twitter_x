from django.urls import path
from .views import home, logout
from . import views
from .views import ComentarioCreateView, ComentarioList, ComentarioUpdate, ComentarioDetail, ComentarioDelete

urlpatterns = [
    path('', home, name='home'),
    path('logout', logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login', views.login_view, name='login'),
    path('login/', views.logincopy_view, name='logincopy'),
    path('Create/', ComentarioCreateView.as_view(), name='criarComentario'),
    path('home', ComentarioList.as_view(), name='listaComentarios'),
    path('update/<int:pk>/', ComentarioUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', ComentarioDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', ComentarioDelete.as_view(), name='delete'),
]

