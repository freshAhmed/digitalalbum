from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib.auth.models import User
from .forms import PostForm
from django.db.models import Q
import logging
# from .models import image_file_handler
log=logging.getLogger(__name__)
# Create your views here.
@login_required
def home_view(request):
    context={}
    user=request.user
    return render (request ,'album.html' , context)
@login_required
def add_post(request):
    form=PostForm((request.POST or None),request.FILES or None)
    if request.method=='POST':
     if form.is_valid():
     
      data=form.clean_Data()   
      post=Post(Title=data.get('Title'),
                description=data.get('description'),
                image=data.get('image'),
                album=data.get('album'))
      post.save()
 
      return redirect('/album') 
    return render(request,'response_api/posts/add_Post.html',{'form':form})
@login_required
def delete_post(request,id):
    if request.method=='POST':
     post=Post.objects.filter(id=id)[0]
     image=str(post.image)
     post.image.delete()
     post.delete()
     return redirect('/album')
    return render(request,'response_api/posts/remove_Post.html',{'post':{'id':id}})

@login_required
def modify_post(request,id):
    post=Post.objects.filter(id=id)[0]
    data=post.get_data()
    form=PostForm(data)
    if request.method=='POST':
     form =PostForm((request.POST or None),request.FILES or None)
     if form.is_valid():
      data=form.clean_Data()
      post.Title=data['Title'] if data['Title'] else post.Title
      post.description=data['description'] if data['description'] else post.description
      post.album=data['album'] if data['album'] else post.album
      image=post.image
      if data['image'] is not None:
        image.delete()
        post.image=data['image'] 
      post.save()  
     return redirect(f'/album/posts/{post.album.id}')
    return render(request,'response_api/posts/edit_Post.html',{'post':post,'form':form})


@login_required
def get_post(request,albumid,postid):
    context={}
    post=Post.objects.filter(Q(id=postid))
    context['post']=post[0]
    return render(request,'response_api/posts/detail_Post.html',context)