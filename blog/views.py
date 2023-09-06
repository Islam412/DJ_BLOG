from django.shortcuts import render , redirect
from .models import Post
from .forms import PostForm


from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
#from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
'''
def Post_List(request):  #quary>Post.objects.all() : template>post_list.htm : context>{'posts':data}
    data = Post.objects.all()
    return render(request , 'post_list.html' ,{'posts':data})
'''
class PostList(ListView): #(template>post_list : context>post_list or object_list)defult for class view
    model = Post



def Post_Detail(request,pk):
    data = Post.objects.get(id=pk)
    return render(request,'blog/post_detail.html',{'post':data})

#class PostDetail(DetailView):
#   model = Post


def add_comment(request):
    pass



'''
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
'''
class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/blog'


'''
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
'''
class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    success_url = '/blog'
    template_name = 'blog/edit_post.html'


'''
def Delete_Post(request,post_id):
    data = Post.objects.get(id=post_id)
    data.delete()
    return redirect('/blog')
'''
class PostDelete(DeleteView):
    model = Post
    success_url = '/blog'