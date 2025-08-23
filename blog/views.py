from django.shortcuts import render

# Create your views here.

posts = [
  {
    'author': 'Jim Kin',
    'title': 'How to get 4.5 GPA',
    'content': 'You need to work and study so hard',
    'date': 'August 25th 2025'
  },
  {
    'author': 'Rasul',
    'title': 'Qanday Unutay menga ham o\'rgat',
    'content': 'Nasini emsin',
    'date': 'August 25th 2025'
  },
  {
    'author': 'Jim Kin',
    'title': 'How to get 4.5 GPA',
    'content': 'I don\'t know',
    'date': 'August 25th 2025'
  },

]

def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})

