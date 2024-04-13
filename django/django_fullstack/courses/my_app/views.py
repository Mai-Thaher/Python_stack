from django.shortcuts import render ,redirect
from . import models
from django.contrib import messages

def index(request):
    context={
        "courses":models.course_info(),
    }
    return render(request, 'index.html',context)

def add_course(request):
    errors=models.Description.objects.basic_validator(request.POST)
    
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    else:
        models.add_course_from_form(request)
        return redirect('/')

def delete_message(request,id):
    context={
        "course":models.specific_course_info(id),
    }
    return render(request, 'delete.html',context)

def cancel_delete(request):
    return redirect('/')

def delete_course(request,id):
    models.delete_selected_course(id)
    return redirect('/')
