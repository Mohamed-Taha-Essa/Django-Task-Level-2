from django.urls import path
from . views import home,arrange 
from .api import ListApiView ,DetailApiView
urlpatterns = [
    path('', home),
    path('arange', arrange),

    # api 
    path('posts/api/' ,ListApiView.as_view()),
    path('posts/api/<int:pk>' ,DetailApiView.as_view()),

]