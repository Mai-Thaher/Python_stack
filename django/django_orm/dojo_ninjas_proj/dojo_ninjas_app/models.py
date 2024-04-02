from typing import Any
from django.db import models
from django.shortcuts import redirect

class Dojo(models.Model):
    name= models.CharField(max_length=255)
    city= models.CharField(max_length=255)
    state= models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Ninja(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    dojo=models.ForeignKey(Dojo, related_name='ninjas', on_delete=models.CASCADE )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def dojo_display():
    return Dojo.objects.all()

# this function will add a new dojo to the database from POST request form
def new_dojo_from_form(request):
    dojo=Dojo.objects.create(name= request.POST['dojo_name'],city=request.POST['city'], state=request.POST['state'] )

# this function will add a new ninja to the database from POST request form 
def new_ninja_from_form(request):
        chosen_dojo=Dojo.objects.get(id = request.POST['dojo'])
        ninja=Ninja.objects.create(first_name= request.POST['f-name'], last_name=request.POST['l-name'], dojo = chosen_dojo )
    
def delete_from_form(request):
    dojo=Dojo.objects.get(id = request.POST['delete_dojo'])
    dojo.delete()
