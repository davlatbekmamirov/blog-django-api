from django.db import models
from user.models import CustomUserModel
from blog.models import BlogModel


class CommentModel(models.Model):
    body = models.CharField(max_length=255)
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='comment_author')
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='comment_blog')
    created_add = models.DateTimeField(auto_now_add=True)


class LikeModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='like_blog')
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='like_author')
    created_add = models.DateTimeField(auto_now_add=True)


class DisLikeModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='dislike_blog')
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='dislike_author')
    created_add = models.DateTimeField(auto_now_add=True)
