from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Posts

# Create your views here.

class PostListView(ListView):
  model = Posts
  template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
  context_object_name = 'posts'
  ordering = ['-date_posted']

class PostDetailView(DetailView):
  model = Posts
  template_name = 'blog/full_post.html' # <app>/<model>_<viewtype>.html
  # context_object_name = 'posts'

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})

