from flask import Flask,render_template,session, redirect
app=Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index_counter():
    if 'counter' not in session:
        session['counter']=0
    session['counter']+=1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect ('/')

@app.route('/add', methods=['POST'] )
def add():
    if 'counter' in session:
        session['counter']+=2
    return redirect('/show')

@app.route('/show')
def show():
    return render_template('index.html')

@app.route('/reset', methods=['POST'] )
def reset():
    return redirect('/destroy_session')

if __name__=="__main__":
    app.run(debug=True)