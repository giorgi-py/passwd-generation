from django.shortcuts import render
from . models import BlogHeader, BlogPost


def blog_home(request):
    headers = BlogHeader.objects.all()
    posts = BlogPost.objects.all().order_by('-created_on')
    return render(request, 'blog_home.html', {'headers': headers, 'posts': posts})







def blog_one(request):
    return render(request, 'blog_one.html')