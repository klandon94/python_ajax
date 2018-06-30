from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages
from .models import User
from django.core import serializers
import json

def index(request):
    return render(request, 'user_login/index.html')

def all_json(request):
    users = User.objects.all()
    return HttpResponse(serializers.serialize('json', users), content_type='application/json')

def all_html(request):
    return render(request, 'user_login/all.html', {'users':User.objects.all()})

def find(request):
    return render(request, 'user_login/all.html', {'users':User.objects.filter(first_name__startswith=request.POST['first_name_starts_with'])})

def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email'], age=request.POST['age'])
    return render(request, 'user_login/all.html', {'users':User.objects.order_by('-id')})