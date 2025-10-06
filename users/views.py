from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCustomForm
from django.contrib.auth.decorators import login_required
from .helper import send_welcome_email
from django.core.mail import send_mail
from django.conf import settings


def register(request):
  if request.method == 'POST':
    form = UserCustomForm(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        send_welcome_email(username=username, email=email)

        messages.success(request, f'{username} your account has been created, You can now log in!')
        return redirect('login')
    else:
      print(form.errors)
  else:
      form = UserCustomForm()
  return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
