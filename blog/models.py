from django.db import models
from django.conf import settings
# Create your models here.


class BlogHeader(models.Model):
    blog_title = models.CharField(verbose_name='BLOG TITLE', max_length=100)
    blog_slug = models.CharField(verbose_name='BLOG SLUG', max_length=200)

    def __str__(self):
        return self.blog_title


class BlogPost(models.Model):
    title = models.CharField(verbose_name='POST TITLE', max_length=100)
    post = models.TextField(verbose_name='POST TEXT')
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title