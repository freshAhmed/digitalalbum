
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import  AuthenticationForm
# class registerForm(ModelForm):


class LoginForm(AuthenticationForm):

 def clean_Data(self):
  if self.is_valid():
   data=self.clean()
   username,password=data['username'],data['password']
   return (username,password)
  return None