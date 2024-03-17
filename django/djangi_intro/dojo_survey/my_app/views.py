from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def get_result(request):
    print(request.POST)
    user_name=request.POST['name']
    user_location=request.POST['location']
    user_gender=request.POST['gender']
    user_language=request.POST.getlist('language')
    user_comment=request.POST['comment']

    context={
        "username":user_name,
        "site":user_location,
        "gender_type": user_gender,
        "selected_languages": user_language,
        "comm":user_comment
    }
    
    request.session['user_info']=context
    request.session['username']=user_name
    request.session['site']=user_location
    request.session['gender_type']=user_gender
    request.session['selected_languages']=user_language
    request.session['comm']=user_comment
    return redirect('/success')

def success(request):
    return render(request, 'show.html', request.session['user_info'])

def go_back(request):
    return redirect ('/')

