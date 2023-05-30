from django.db import models
from user.models import CustomUserModel


class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=1000)
    summary = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='author_blog')
    created_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
