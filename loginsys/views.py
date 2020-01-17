from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.generic.base import View

from django.core import *

# Create your views here.

def login(request):
    if request.POST:
        print(request)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login/index.html', )
            #return render(request, 'login/index.html',)

    else:
        return render(request, 'login/index.html')

def logout(request):
    print(request)
    auth.logout(request)
    return redirect('../../loginsys/login/')

#def logout(request):
   # return render(request, 'logn.html')
