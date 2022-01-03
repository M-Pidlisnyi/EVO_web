import re
from django.contrib import auth
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls.conf import path


def index(request):
    logout(request)
    username = password = ''
    wrong_password = False
    if request.method == 'POST':

        if request.POST.get('username', False):
            username = request.POST.get('username')
        if request.POST.get('password', False):
            password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            if User.objects.filter(username = username).first():
                wrong_password = True
                return render(request, 'index.html', context={'wrong_password': wrong_password})
            user = User.objects.create_user(username=username, password=password)
            user.save()
            
            login(request, user)
            return redirect('hello/?new=1')
        else:
            if user.is_active:
                login(request, user)
                return redirect('hello/?new=0')

    return render(request, 'index.html')

def hello(request):
    is_new_user = False
    if request.method == 'GET':
        new = request.GET.get('new', False)
        is_new_user = bool(int(new))

    return render(request, 'hello.html', context={'is_new_user': is_new_user})

def visitors(request):
    all_visitors = User.objects.all()
    visitors_num = all_visitors.count()
    
    context = {
        'all_visitors': all_visitors,
        'visitors_num': visitors_num
    }

    return render(request, 'visitors.html', context=context)