from django.shortcuts import render,redirect

def index(request):
    if 'counter' not in request.session:
        request.session['counter']=0
    request.session['counter']+=1
    return render(request, 'index.html')

def add_on(request):
    if 'counter' in request.session:
        request.session['counter']+=2
    return redirect('/show')
def show(request):
    return render(request, 'index.html')

def destroy(request):
    del request.session['counter']
    return redirect('/')
