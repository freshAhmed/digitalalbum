from django.shortcuts import render
from django.contrib.auth.forms import  AuthenticationForm
import logging

log=logging.getLogger(__name__)
def login_view(request,*args,**kwargs):
    form=AuthenticationForm(request.POST or None)
    log.info(request.POST)
    if request.method=="POST":
     log.info(form.data)
    return render (request,'accounts/login.html',{'form':form})
    


def logout_view(request,*args,**kwargs):
    return render(request,'base.html',{})



def register(request,*args,**kwargs):
    return render(request,'base.html',{})