from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 50)
    content = models.TextField()

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment =  models.CharField(max_length =100)
    author = models.CharField(max_length =50,)
    created_at = models.DateTimeField(auto_now_add=True)

class User(AbstractUser):
    # Add your custom fields here
    age = models.PositiveIntegerField(null=True, blank=True)
    is_author = models.BinaryField(default = 0)
    subscribers = models.JSONField(default = [])
    # Add more fields as needed
