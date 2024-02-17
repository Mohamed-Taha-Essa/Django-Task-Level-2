from django.urls import path
from . views import home,arrange
urlpatterns = [
    path('', home),
    path('arange', arrange),
    # path('add_comment/<int:pk>', add_comment),
]