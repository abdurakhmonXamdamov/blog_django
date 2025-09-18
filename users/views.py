from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCustomForm

def register(request):
  if request.method == 'POST':
    form = UserCustomForm(request.POST)
    if form.is_valid:
        form.save()
        username = form.cleaned_data.get('first_name')
        messages.success(request, f'Account is created for {username}! You can now log in')
        return redirect('blog-home')
  else:
      form = UserCustomForm()
  return render(request, 'users/register.html', {'form': form})

# we got different types of messages:

# messages.info
# messages.success
# messages.debug
# messages.warning
# messages.error