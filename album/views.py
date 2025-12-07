from django.shortcuts import render

# Create your views here.
def create_album(request,*args,**kwargs):
    return render(request,'base.html',{})


def get_album(request,*args,**kwargs):
    return render(request,'base.html',{})

def delete_album(request,*args,**kwargs):
    return render(request,'base.html',{})