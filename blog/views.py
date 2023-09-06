from django.shortcuts import render
from .models import Post
# Create your views here.

def Post_List(request):
    data = Post.objects.all()
    return render(request , 'post_list.html' ,{'posts':data})


def Post_Detail(request,post_id):
    data = Post.objects.get(id=post_id)
    return render(request,'post_detail.html',{'post':data})