from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
# Create your views here.

def index_page(request):
    return render(request, 'homepage/index.html', {'username':auth.get_user(request).username})

def articles(request):
    return render(request, 'homepage/articles.html', {'username':auth.get_user(request).username})