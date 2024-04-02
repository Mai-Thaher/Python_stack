from django.shortcuts import render, redirect
from. import models

def index(request):
    context={ "dojos": models.dojo_display(),
    }
    return render(request, 'index.html', context)

# this function will add a new dojo to the database from POST request form
def add_dojo(request):
    models.new_dojo_from_form(request)
    return redirect('/')

# this function will add a new ninja to the database from POST request form 
def add_ninja(request):
    models.new_ninja_from_form(request)
    return redirect('/')

def delete(request):
    models.delete_from_form(request)
    return redirect('/')

    