from . models import Post ,Comment

from .serializers import PostSerializer ,CommentSerializer

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class ListApiView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class =PostSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['author', 'draft']
    search_fields = ['title', 'content']
    ordering_fields =['public_date_time']


class DetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class =PostSerializer

    


