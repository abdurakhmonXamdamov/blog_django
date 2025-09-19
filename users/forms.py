from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCustomForm(UserCreationForm):
  # first_name = forms.CharField(max_length=30, required=True)
  # last_name = forms.CharField(max_length=30, required=True)
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

  # def save(self, commit=True):
  #       user = super().save(commit=False)
  #       user.username = self.cleaned_data['first_name']
  #       if commit:
  #           user.save()
  #       return user

