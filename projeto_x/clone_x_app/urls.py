from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('home', home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout', views.login_view, name='logout'),
]