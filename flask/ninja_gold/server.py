from flask import Flask, render_template, session, request, redirect
import random
from datetime import datetime
app=Flask(__name__)
app.secret_key = 'keep it secret'

@app.route('/')
def index():
    if 'money' not in session:
        session['total']=0
    if 'activities' not in session:
        session['activities']=[]
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    
    if request.form['building']=='farm':
        earning=random.randint(10,20)
        session['money']=int(earning)
        session['building']='farm'

    elif request.form['building']=='cave':
        earning=random.randint(5,10)
        session['money']=int(earning)
        session['building']='cave'
        
    elif request.form['building']=='house':
        earning=random.randint(2,5)
        session['money']=int(earning)
        session['building']='house'
        
    else:
        earning=random.randint(-50,50)
        session['money']=int(earning)
        session['building']='casino'
    if 'money' in session:
        if session['money']>0:
            session['activities'].append(f"Earned {session['money']} golds from the {session['building']}! {datetime.now().strftime("%m/%d/%Y, %H:%M %p")}" ) 
        else:
            session['activities'].append(f" Entered a casino and lost {abs(session['money'])} golds ... Ouch!.. {datetime.now().strftime("%m/%d/%Y, %H:%M %p")}" )
    print(session['activities'])       
    if 'money' in session:
        session['total']+=session['money']

    return redirect('/')

@app.route("/restart")
def restart_game():
    session.clear()
    return redirect("/")

if __name__=='__main__':
    app.run(debug=True)