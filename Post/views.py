from django.shortcuts import render,redirect
from .models import Post
from .froms import PostForm
import logging
log=logging.getLogger(__name__)
# Create your views here.
def home_view(request):
    context={}
    posts=Post.objects.all()
    context['posts']=posts
 
    return render (request ,'album.html' , context)

def add_post(request):

    form=PostForm((request.POST or None),request.FILES or None)
    if request.method=='POST':
        if form.is_valid():
         data=form.clean_Data()   
         post=Post(Title=data.get('Title'),description=data.get('description'),image=data.get('image'))
         post.save()

         return redirect('/posts') 

    return render(request,'response_api/add_Post.html',{'form':form})
    
def delete_post(request,id):
    if request.method=='POST':
     post=Post.objects.filter(id=id)[0]
     image=str(post.image)
     post.image.delete()
     post.delete()
     return redirect('/posts')
    
    return render(request,'response_api/remove_Post.html',{'post':{'id':id}})


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
        image=post.image
        if data['image'] is not None:
            image.delete()
            post.image=data['image'] 
        post.save()  
     return redirect('/posts')
    return render(request,'response_api/edit_Post.html',{'post':post,'form':form})



def get_post(request,id):
    context={}
    post=Post.objects.filter(id=id)
    context['post']=post.first()
    return render(request,'response_api/detail_Post.html',context)