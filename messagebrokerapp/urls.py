# accounts/urls.py
from django.urls import path
from . import views
from .models import User,Post,Comment
urlpatterns = [
    path('createposts', views.createposts, name='createposts'),
    path('createcomment',views.createcomment,name = 'createcomment'),
    path('createuser',views.createuser,name = 'createuser'),
    path('addsubscribers',views.add_subscribers,name = 'addsubscribers'),
]

