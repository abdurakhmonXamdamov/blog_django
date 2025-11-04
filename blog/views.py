from django.shortcuts import render, get_object_or_404
from .models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #for restricting access to the view to only logged in users
from .forms import PostForm
from django.contrib.auth.models import User
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

  paginate_by = 5

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['title'] = 'Home'
      return context

class UserPostListView(ListView):
  model = Posts
  template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
  context_object_name = 'posts'
  paginate_by = 5

  def get_queryset(self):
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Posts.objects.filter(author=user).order_by('-date_posted')

  

class PostDetailView(DetailView):
  model = Posts
  template_name = 'blog/full_post.html' # <app>/<model>_<viewtype>.html
  # context_object_name = 'posts'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['title'] = f"{self.object.title} - Blog"
      return context

class PostCreateView(LoginRequiredMixin,CreateView):
  model = Posts
  form_class = PostForm

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['title'] = 'Create New Post'
      return context
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

