from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import LoginForm
import logging

log=logging.getLogger(__name__)
def login_view(request,*args,**kwargs):
    form=LoginForm((request.POST or None))
    if request.method=="POST":
     username=request.POST ['username']
     password=request.POST['password'] 
     user=authenticate(username=username,password=password)
     if user:
      login(request,user)
      return redirect('/posts') 
    return render (request,'accounts/login.html',{'form':form})
    


def logout_view(request,*args,**kwargs):
    log.info( 'next' in request.GET)     
    if request.method=='POST':
     if request.user is not None:
      logout(request)
      if 'next' in request.GET:
       next_url=request.GET.get('next')
       return redirect(next_url)
    return render(request,'accounts/logout.html',{})



def register(request,*args,**kwargs):
    form =UserCreationForm(request.POST or None)
    if request.method=='POST':
      if form.is_valid():
       data=form.clean()
       form.save()
       user= User.objects.filter(username=data['username'])
       form=UserCreationForm()
       form.error_messages='this username has been create chose anthor username' if user is not None else form.error_messages
       return redirect('/login/')
    return render(request,'accounts/register.html',{'form':form})