from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from home.models import ContactFormsModel

# Create your views here.


def home(request):
    return render(request,'index.html',{})


def about(request):
    return render(request,'about.html',{})


def contact(request):
    if request.method == 'POST':
        db_data = {
            'name' : request.POST.get('name'),
            'email' : request.POST.get('email'),
            'subject' : request.POST.get('subject'),
            'message' : request.POST.get('message')
        }
        ContactFormsModel.objects.create(**db_data)
    return render(request, 'contact.html')
