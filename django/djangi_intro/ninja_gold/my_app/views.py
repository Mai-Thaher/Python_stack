from django.shortcuts import render, redirect
import random
import datetime


def index(request):
    if 'money' not in request.session:
        request.session['total']=0
    if 'activities' not in request.session:
        request.session['activities']=[]
    return render(request, 'index.html')

def process_money(request):
    if request.POST['building']=='farm':
        earning=random.randint(10,20)
        request.session['money']=int(earning)
        request.session['building']='farm'

    elif request.POST['building']=='cave':
        earning=random.randint(10,20)
        request.session['money']=int(earning)
        request.session['building']='cave'
        
    elif request.POST['building']=='house':
        earning=random.randint(10,20)
        request.session['money']=int(earning)
        request.session['building']='house'
        
    else:
        earning=random.randint(-50,50)
        request.session['money']=int(earning)
        request.session['building']='quest'
    if 'money' in request.session:
        if request.session['money']>0:
            if request.session['building']=='quest':
                request.session['activities'].append(f"You completed a quest and Earned {request.session['money']} gold. ({datetime.datetime.now().strftime("%B %d %Y %I:%M%p")})")
            else:
                request.session['activities'].append(f"You entered a {request.session['building']} and Earned {request.session['money']} gold. ({datetime.datetime.now().strftime("%B %d %Y %I:%M%p")})")  
        else:
            request.session['activities'].append(f"You failed a quest and lost {abs(request.session['money'])} golds. Ouch!.({datetime.datetime.now().strftime("%B %d %Y %I:%M%p")})")
    print(request.session['activities'])       
    if 'money' in request.session:
        request.session['total']+=request.session['money']

    return redirect('/')

def restart_game(request):
    del request.session['money']
    del request.session['building']
    del request.session['activities']
    return redirect("/")
