from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    return render_template("checkout.html",strawberry_q=request.form['strawberry'],
                            raspberry_q=request.form['raspberry'],
                            apple_q=request.form['apple'],
                            fname=request.form['first_name'],
                            lname=request.form['last_name'],
                            IDnum=request.form['student_id'], 
                            count=int(request.form['strawberry'])+int(request.form['raspberry'])
                            +int(request.form['apple']))

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    