from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from requests import request
# Create your views here.
from .models import Post, Comment, User


@api_view(['POST','GET'])
def add_post(request):
    try:
        blog_id = None
        blog_status = False
        content = request.POST.get("post","")
        title = request.POST.get("title","")
        blog_post = Post(content = content,title = title)
        if blog_post:
            blog_post.save()
            blog_id = blog_post.post_id
        if blog_id:
            blog_status = True
        return JsonResponse({"blog_created":blog_status,"blog_id":blog_id})
    except Exception as error:
        return JsonResponse({"blog_created":False,"blog_id":None})


@api_view(['POST','GET'])
def add_comment(request):
    try:
        blog_comment_id = None
        blog_id = request.POST.get("blog_id", False)
        comment = request.POST.get("comment",False)
        if not blog_id:
            return JsonResponse({"Missing Parameter":"Blog Id"})
        if not comment:
            return JsonResponse({"Missing Parameter":"Comment"})
        if not Post.objects.filter(post_id = blog_id).exists():
            return JsonResponse({"Error":"No Such Blog Exists"})
        blog_comment = Comment(post_id = blog_id,title = comment)
        if blog_comment:
            blog_comment.save()
            blog_comment_id = blog_comment.post_id
        return JsonResponse({"comment_added":True,"comment_id":blog_comment_id})
    except Exception as error:
        return JsonResponse({"comment_added":False,"comment_id":blog_comment_id})
    

@api_view(['POST','GET'])
def add_user(request):
    try:
        username = request.POST.get("username", False)
        email = request.POST.get("email", False)
        password = request.POST.get("password", False)
        is_author =int(request.POST.get("password", 0))
        if not(username and email and password and is_author):
            return JsonResponse({"One or More Missing Parameter":True})
        user = User(username=username,email=email,password=password,is_author=is_author)
        if user:
            user.save()        
            return JsonResponse({"user_added":True, "user_id":user.id, "username":user.username, "is_author":is_author})
        return JsonResponse({"user_added":False})
    except Exception as error:
        return JsonResponse({"user_added":False})
    


@api_view(['POST','GET'])
def add_subscribers(request):
    try:
        author_user_id = request.POST.get("author_user_id", False)
        subscriber_user_id = request.POST.get("subscriber_user_id", False)
        if not(author_user_id and subscriber_user_id):
            return JsonResponse({"One or More Missing Parameter":True}) 
        if not(User.objects.filter(id=author_user_id).exists()):
            return JsonResponse({"Error Occured":"Author Doesn't Exits"})
        if not(User.objects.filter(id=subscriber_user_id).exists()):
            return JsonResponse({"Error Occured":"Subscriber Doesn't Exits"})
        user = User.objects.get(id = author_user_id)
        user.subscribers = user.subscribers.append(subscriber_user_id)
        user.save()
        return JsonResponse({"subscriber_added":True})
    except Exception as error:
        return JsonResponse({"subscriber_added":True})
    

