from django.urls import path
from .views import home, logout
from . import views

urlpatterns = [
    path('home', home, name='home'),
    path('logout', logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
]