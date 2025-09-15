from django.shortcuts import render
from datetime import datetime
from .models import Posts

# Create your views here.

def home(request):
  context = {
    'posts': Posts.objects.all()
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})

