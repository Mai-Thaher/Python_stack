from flask import Flask
app=Flask(__name__)
@app.route("/")
def say_hello():
    return "Hello World!"
@app.route("/dojo")
def say_dojo():
    return "Dojo!"
@app.route("/say/<name>")
def say_hi(name):
    return f"Hi {name}"
@app.route("/repeat/<int:number>/<string:word>")
def repeat_word(number,word):
    return word*number
    
if __name__=="__main__":
    app.run(debug=True)
