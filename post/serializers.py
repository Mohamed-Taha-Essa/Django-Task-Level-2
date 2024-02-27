from rest_framework import serializers
from .models import Post ,Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields=['id','username','email']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
       model =Comment 
       fields = ['comment']
class PostSerializer(serializers.ModelSerializer):
    author =UserSerializer()
    comment = CommentSerializer( many =True ,source='comment_posts')
    class Meta:
        model = Post
        fields= ['author' ,'title' ,'content','draft','image','public_date_time',
                 'comment']
