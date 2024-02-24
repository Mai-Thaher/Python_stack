from flask import Flask, render_template
app=Flask(__name__)

@app.route('/play')
def display_3boxes():
    return render_template('index.html',num=3)

@app.route('/play/<int:times>')
def display_multible_boxes(times):
    return render_template('index.html',num=times)

@app.route('/play/<int:times>/<color>')
def display_colored_boxes(times,color):  
    return render_template('index.html',num=times,background_color=color)

if __name__=="__main__":
    app.run(debug=True)