# accounts/urls.py
from django.urls import path
from . import views
from .models import User,Post,Comment
urlpatterns = [
    path('createposts', views.add_post, name='createposts'),
    path('createcomment',views.add_comment,name = 'createcomment')
]
