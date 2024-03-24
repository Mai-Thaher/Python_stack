from django.shortcuts import render, redirect
from .models import User
from . import models

def index(request):
    models.edit_user()
    context={
        "user_info":User.objects.all()
    }
    return render(request, 'index.html',context)

def add_user(request):
    models.new_user_from_form(request)
    return redirect('/') 
