from flask import Flask, render_template
import math
app=Flask(__name__)

@app.route('/')
def index_checkerboard():
    return render_template('index.html',x=int(8),y=int(8),color1='red',color2='black')

@app.route('/<int:x>')
def display_xraws_checkerboard(x):
    return render_template('index.html', x=int(x),y=int(8),color1='red',color2='black')

@app.route('/<int:x>/<int:y>')
def display_different_checkerboard(x,y):
    return render_template('index.html', x=int(x),y=int(y),color1='red',color2='black')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def display_colored_checkerboard(x,y,color1, color2):
    return render_template('index.html', x=int(x),y=int(y),color1=color1, color2=color2 )
if __name__=="__main__":
    app.run(debug=True)