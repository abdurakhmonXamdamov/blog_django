from django.shortcuts import render

# Create your views here.

posts = [
  {
    'author': 'Jim Kin',
    'title': 'How to get 4.5 GPA',
    'content': 'You need to work and study so hard, Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel,',
    'date': 'August 25th 2025'
  },
  {
    'author': 'Rasul',
    'title': 'Qanday Unutay menga ham o\'rgat',
    'content': 'Nasini emsin, Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel,',
    'date': 'August 25th 2025'
  },
  {
    'author': 'Jim Kin',
    'title': 'How to get 4.5 GPA',
    'content': 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, ',
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

