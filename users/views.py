from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCustomForm
from django.contrib.auth.decorators import login_required


def register(request):
  if request.method == 'POST':
    form = UserCustomForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Your account has been created, You can now log in!')
        return redirect('login')
    else:
      print(form.errors)
  else:
      form = UserCustomForm()
  return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')




# we got different types of messages:

# messages.info
# messages.success
# messages.debug
# messages.warning
# messages.error