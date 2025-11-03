from django.shortcuts import render
from .models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #for restricting access to the view to only logged in users
from .forms import PostForm
from django.views.generic import (
  ListView, 
  DetailView,
  CreateView,
  UpdateView,
  DeleteView,
)

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

class PostCreateView(LoginRequiredMixin,CreateView):
  model = Posts
  form_class = PostForm

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Posts
  form_class = PostForm

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author: return True
    return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Posts
  template_name = 'blog/post_confirm_delete.html'
  success_url = '/'

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author: return True
    return False

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})

