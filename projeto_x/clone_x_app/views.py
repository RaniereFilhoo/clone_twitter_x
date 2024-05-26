from django.shortcuts import render
from .models import Home

def home(request):
    posts = Home.objects.all()
    return render(request, 'clone_x_app/home.html', {'posts': posts})
