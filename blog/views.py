from django.shortcuts import render , redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def Post_List(request):
    data = Post.objects.all()
    return render(request , 'post_list.html' ,{'posts':data})


def Post_Detail(request,post_id):
    data = Post.objects.get(id=post_id)
    return render(request,'post_detail.html',{'post':data})


def New_Post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/blog')
    else:
        form = PostForm()
    return render(request,'new_post.html',{'form':form})


def Edit_Post(request,post_id):
    data = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/blog')
    else:
        form = PostForm(instance=data) #instance بتعامل مع داتا كذا
    return render(request,'edit_post.html',{'form':form})


def Delete_Post(request,post_id):
    data = Post.objects.get(id=post_id)
    data.delete()
    return redirect('/blog')
