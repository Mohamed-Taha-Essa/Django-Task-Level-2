from django.shortcuts import render ,redirect
from .models import Post ,Comment
from .forms import PostForm ,CommentForm
# Create your views here.


def home(request):
    posts = Post.objects.all()
    # comments = Comment.objects.all()
   
    if request.method =='POST' :
        id = int(request.POST['post_id'])
        post = Post.objects.get(id = id)
        form =CommentForm(request.POST)
        if form.is_valid():
            myform =  form.save(commit=False)
            myform.post =post
            myform.user = request.user
            myform.save()
            return redirect(f'/home')
    else:
        form =CommentForm()

    return render(request , 'post/home.html' ,{
        'posts':posts,
        'form':form,
        # 'comments':comments
        })

# def add_comment(request,pk):
#     post_data =Post.objects.get(id =pk)

#     if request.method =='POST' :
#             form =CommentForm(request.POST)
#             if form.is_valid():
#                 myform =  form.save(commit=False)
#                 myform.post =post_data
#                 myform.save()
#                 return redirect(f'/posts')
#             else:
#                 form =CommentForm()
#     return render(request , 'post/home.html' ,{'form':form})

