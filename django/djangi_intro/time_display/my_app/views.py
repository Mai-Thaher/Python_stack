from django.shortcuts import render, redirect
from time import gmtime, strftime
    
def index(request):
    context = {
        "time": strftime(" %H:%M %p", gmtime()),
        "date":strftime("%b %d %Y", gmtime())
    }
    return render(request,'index.html', context)
def time_display(request):
    return redirect('/')


