from django.db import models
from django.shortcuts import render, redirect
import random

def random_number(request):
    random_num=random.randint(1,100)
    print(random_num) 
    request.session['number']=random_num
    request.session['attempt']=0

def result(request):
    request.session['guess_number']=int(request.POST['guess'])
    if 'guess_number' not in request.session:
        request.session['attempt']=0
    request.session['attempt']+=1

def too_high(request):
    if request.session['guess_number'] > request.session['number']:
        request.session['result']='too high!'

def too_low(request):
    if request.session['guess_number'] < request.session['number']:
        request.session['result']='too low!'

def correct_answer(request):
    if request.session['guess_number'] == request.session['number']:
        request.session['result']='was the number!'
    
