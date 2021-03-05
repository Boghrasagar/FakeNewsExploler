from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

# Create your views here.


def home(request):
    return render(request,'index.html',{})


def about(request):
    return render(request,'about.html',{})


def contact(request):
    return render(request, 'contact.html')
