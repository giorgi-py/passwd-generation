from django.shortcuts import render
import random

def home_view(request):
    return render(request, 'home/home.html')

def password(request):
    chars = list('abcdefghigklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIGKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        chars.extend(list('!@#$%^&'))
    if request.GET.get('numbers'):
        chars.extend('1234567890')
    length = int(request.GET.get('length'))
    thepass = ''
    for i in range(length):
        thepass += random.choice(chars)
    return render(request, 'home/password.html', {'pass': thepass})