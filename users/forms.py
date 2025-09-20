from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm # for login purposes

class UserCustomForm(UserCreationForm):
  # first_name = forms.CharField(max_length=30, required=True)
  # last_name = forms.CharField(max_length=30, required=True)
  email = forms.EmailField(
    widget= forms.EmailInput(attrs={
      'class': 'form-control',
      'placeholder': 'Enter your valid email'
    })
  )

  username = forms.CharField(
    widget= forms.TextInput(attrs={
      'class': 'form-control',
      'placeholder': 'Enter unique Username'
    })
  )

  password1 = forms.CharField(
    widget= forms.PasswordInput(attrs={
      'class' : 'form-control',
      'placeholder': 'Enter your password'
    })
  )

  password2 = forms.CharField(
    widget= forms.PasswordInput(attrs={
      'class' : 'form-control',
      'placeholder': 'Confirm your password'
    })
  )

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']



class UserLoginForm(AuthenticationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    for name, field in self.fields.items():
      field.widget.attrs['class'] = 'form-control'
      field.widget.attrs['placeholder'] = f'Enter {field.label}'