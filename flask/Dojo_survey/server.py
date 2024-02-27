from flask import Flask, render_template,request
app=Flask(__name__)

@app.route('/')
def index_servey():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def submit():
    print("*"*50)
    print(request.form)
    #selected_options=[]
    #for option in ['language-1','language-2','language-3','language-4']:
    selected_language=request.form.getlist('language')
    return render_template('info.html',username=request.form['name'],
                            site=request.form['location'], 
                            gender_type=request.form['gender'], 
                            selected_options=selected_language, 
                            comm=request.form['comment'])

if __name__=="__main__":
    app.run(debug=True)