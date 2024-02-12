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
    pass
    

@api_view(['POST','GET'])
def add_user(request):
    pass