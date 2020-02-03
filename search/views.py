from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.generic.base import View

from django.core import *


# Create your views here.

def search(request):
        return render(request, 'search/search.html')

# def logout(request):
# return render(request, 'logn.html')
