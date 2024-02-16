from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author =models.ForeignKey(User, related_name='post_author'  ,  on_delete=models.CASCADE)
    title = models.CharField( max_length=50)
    content=models.TextField(max_length=20000)
    draft =models.BooleanField(default=True)

    public_date_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post')


    def __str__(self):
        return self.title



class Comment(models.Model):
    #relation ship between comment and post  one to many 
    # one post have mulible comment.
    #when add comment determine the post
    post = models.ForeignKey(Post, related_name='comment_posts', on_delete=models.SET_NULL ,null=True)

    user = models.CharField( max_length=50)
    comment= models.TextField(max_length=100)
    created_at = models.DateTimeField( default= timezone.now )
    
    def __str__(self):
        return self.user
    