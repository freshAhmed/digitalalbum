from django.shortcuts import render
from .models import albumModel
from Post.models import Post
from django.contrib.auth.decorators import login_required
import logging
from django.db.models import Q
log=logging.getLogger(__name__)
# Create your views here.
def create_album(request,):
    return render(request,'base.html',{})

@login_required
def get_album(request,albumid):
    album=albumModel.objects.filter((Q(id=albumid)& Q(author=request.user)))
    post=album[0].get_post(Post)
    return render(request,'response_api/album/detail_album.html',{'album':album[0],'posts':post})

def delete_album(request,albumid):
    return render(request,'base.html',{})

def edit_album(request,albumid):
    return render(request,'base.html',{})


@login_required
def get_albums(request):
    context={}
    albums=albumModel.objects.filter(Q(author=request.user))
    context['albums']=albums
    return render(request,'album.html',context)