from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from requests import request
# Create your views here.



@api_view(['POST','GET'])
def add_post(request):
    pass





@api_view(['POST','GET'])
def add_comment(request):
    pass
    