from flask import Flask, render_template, session,request,redirect
import random
app=Flask(__name__)
app.secret_key='keep it secure'

@app.route('/')
def index():
    x=random.randint(1,100)
    print(x)
    session['number']=x
    session['attempt']=0
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    session['guess_number']=int(request.form['guess'])
    
    if 'guess_number' not in session:
        session['attempt']=0
    session['attempt']+=1
    if session['attempt'] == 5:
        return redirect('/lose')
    return redirect('/show')

@app.route('/lose')
def lose():
    return render_template('lose.html')

@app.route('/tryagain', methods=['POST'])
def tryagain():
    return redirect('/')    

@app.route('/show')
def show():
    return render_template('show.html')

@app.route('/again', methods=['POST'])
def play_again():
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)