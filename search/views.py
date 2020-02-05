from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.generic.base import View
from .models import Equipment
from django.core import *


# Create your views here.

def search(request):
        iteams = []
        for p in Equipment.objects.raw('SELECT * FROM homepage_equipment'):
                iteams.append(p)
        return render(request, 'search/search.html', {'username': auth.get_user(request).username, 'results': iteams})

# def logout(request):
# return render(request, 'logn.html')
