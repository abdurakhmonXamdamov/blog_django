from django.shortcuts import render
from .models import Posts

# Create your views here.

def home(request):
  context = {
    'posts': Posts.objects.all()
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})

def posts(request):
  return render(request, 'blog/full_post.html')
