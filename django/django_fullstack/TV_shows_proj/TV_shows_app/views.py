from django.shortcuts import render, redirect
from . import models
from .models import TV_show
from django.contrib import messages

def index(request):
    return redirect('/shows')

# This func return all the TV shows in the database and display it in a table(homepage) 
def display_all_shows(request):
    context={
        "shows":models.display_shows()
    }
    return render(request, 'shows.html', context)

# This func will delete the TV show from the database
def delete_show(request,id):
    models.delete(id)
    return redirect('/shows')

# This func will display the details for the selected show
def display_show(request,id):
    context={
        "show":models.show_info(id)
    }
    return render (request, 'info.html',context)

# This func will display a form for adding new show (GET method)
def add_show_form(request):
    return render(request, 'new_show.html')  

# This func is for adding a new show (POST method) + loop through errors from validator func
def add_new_show(request):
    if request.method == 'POST':
        errors=models.TV_show.objects.show_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/shows/new')
        else:
            show=models.new_show(request)
            return redirect(f'/shows/{show.id}') 

# This func will display a form for editting new show (GET method)
def edit_form(request,id):
    context={
        "show":models.show_info(id)
    }
    return render(request, 'edit.html',context)

# This func is for updating aspecific show (POST method) + loop through errors from validator func
def update_show(request,id):
    errors=models.TV_show.objects.show_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect (f'/shows/{id}/edit')
    else:
        models.update(request,id)
        return redirect(f'/shows/{id}')
