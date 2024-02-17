from django.shortcuts import render ,redirect
from .models import Post ,Comment
from .forms import PostForm ,CommentForm ,ArrangeForm
# Create your views here.


def home(request):
    posts = Post.objects.all()
    # comments = Comment.objects.all()
    comments = None
    if request.method =='POST' :
        
        form =CommentForm(request.POST)
        form2 =ArrangeForm(request.POST)

        if form.is_valid():
            id = int(request.POST['post_id'])
            post = Post.objects.get(id = id)
            myform =  form.save(commit=False)
            myform.post =post
            myform.user = request.user
            myform.save()
            return redirect(f'/home')
        
        if form2.is_valid():
            print('form2')
            id = int(request.POST['post_arrange_id'])
            post = Post.objects.get(id = id)
            selected_choice = form2.cleaned_data['arrange']

            if selected_choice == 'Ascending' :
                print('ascending')
                comments=  Comment.objects.filter(post = post).order_by('created_at')
            elif selected_choice == 'Deascending' :
                comments = Comment.objects.filter(post = post).order_by('-created_at')
                print('deascending')
            else :
                comments =None
            
            # return redirect(f'/home')
    else:
        form =CommentForm()
        form2 = ArrangeForm()

    return render(request , 'post/home.html' ,{
        'posts':posts,
        'form':form,
        'form2':form2,       
        'comments':comments
        })

def arrange(request):
    if request.method =='POST' :
        form2 =ArrangeForm(request.POST)
        id = int(request.POST['post_arrange_id'])
        post = Post.objects.get(id = id)
        if form2.is_valid():
            selected_choice = form2.cleaned_data['arrange']
            comments = Comment.objects.filter(post = post)

            if selected_choice == 'Ascending' :
                comments = comments.order_by('created_at')
            elif selected_choice == 'Deascending' :
                comments = comments.order_by('-created_at')
            else :
                comments =None
            form2.save()
            return redirect(f'/home')
    else:
        form2 =ArrangeForm()
    return render(request , 'post/home.html' ,{ 
        'form2':form2,
        'comments':comments
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

