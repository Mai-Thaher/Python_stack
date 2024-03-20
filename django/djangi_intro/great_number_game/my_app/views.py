from django.shortcuts import render, redirect
from . import models

# description: this function give a random number between 1 and 100 and save it in a session
def index(request):
    models.random_number(request)
    return render(request, 'index.html')

def display_result(request):
    models.result(request)
    models.too_high(request)
    models.too_low(request)
    models.correct_answer(request)
    if request.session['attempt'] == 5:
        return redirect('/lose')
    return render(request, 'show.html')

def lose(request):
    return render(request, 'lose.html')

def try_again(request):
    return redirect ('/')


