from django.urls import path
from . views import home
urlpatterns = [
    path('', home),
    # path('add_comment/<int:pk>', add_comment),
]